from django.db import models
from django.core.files import File
from PIL import Image
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import qrcode
import io
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from django.db.models import Max
# Create your models here.
class Supplier(models.Model):
	name = models.CharField(max_length = 200)
	address = models.TextField(default = None, null = True, blank = True)
	contact = models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.name

class RequestingEndUser(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class FundSource(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class ModeOfProcurement(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class PurchaseOrder(models.Model):
	date = models.DateField()
	series = models.PositiveIntegerField()
	supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE, null = True)
	requesting_end_user = models.ForeignKey(RequestingEndUser, on_delete = models.CASCADE, null = True)
	date_received_by_supplier = models.DateField(null = True)
	date_received_from_bac = models.DateField(null = True)
	term_of_delivery = models.PositiveIntegerField(null = True)
	mode_of_procurement = models.ForeignKey(ModeOfProcurement, on_delete = models.CASCADE, null = True)
	fund_source = models.ForeignKey(FundSource, on_delete = models.CASCADE, null = True)
	amounts = models.FloatField(null = True)
	remarks = models.TextField(null = True)
	date_recorded = models.DateField(default = timezone.now, null = True)

	@property
	def po_no(self):
		md = self.date.strftime("%m%d")
		y = self.date.strftime("%y")
		series = self.series
		return f'{md}-{str(series).zfill(3)}-{y}'

	def __str__(self):
		return self.po_no

	@property
	def supplier_name(self):
		return self.supplier.name

	@property
	def date_to_deliver(self):
		if self.date_received_by_supplier is not None:
			return self.date_received_by_supplier + datetime.timedelta(days = self.term_of_delivery)
		else:
			return None


class Campus(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class ReceiveStatus(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class InspectionOfficer(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class RequisitioningOffice(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name


class Inspection(models.Model):
	date = models.DateField(default = datetime.datetime.now)
	series = models.PositiveIntegerField(null = True)
	po = models.ForeignKey(PurchaseOrder, on_delete = models.CASCADE)
	requisitioning_office = models.ForeignKey(RequisitioningOffice, on_delete = models.CASCADE)
	campus = models.ForeignKey(Campus, on_delete = models.CASCADE)
	date_received = models.DateField()
	purpose = models.TextField(null = True, blank = True)
	receive_status = models.ForeignKey(ReceiveStatus, on_delete = models.CASCADE)
	inspection_officer = models.ForeignKey(InspectionOfficer, on_delete = models.CASCADE)
	with_acc_codes = models.BooleanField(default = False)
	inspection_date = models.DateField(default = datetime.datetime.now)

	@property
	def ins_no(self):
		d = datetime.datetime.combine(self.date, datetime.datetime.min.time())
		mdy = d.strftime("%m%d%y")
		s = str(self.series).zfill(3)
		camp = self.campus.name
		return f'{mdy}-{s}-({camp[0].title()}I)'
	

	def __str__(self):
		return self.ins_no

class ReceiptType(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Receipt(models.Model):
	type = models.ForeignKey(ReceiptType, on_delete = models.CASCADE)
	no = models.CharField(max_length = 100)
	date = models.DateField()
	inspection = models.ForeignKey(Inspection, on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.no} ({self.type})'

class Unit(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class AccountCode(models.Model):
	code = models.CharField(max_length = 20)
	title = models.CharField(max_length = 254)

	def __str__(self):
		return f'{self.title} ({self.code})'

	class Meta:
		ordering = ['title']
	
class Article(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Classification(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Item(models.Model):
	no = models.PositiveIntegerField(null = True)
	article = models.ForeignKey(Article, on_delete = models.CASCADE, null = True)
	desc = models.CharField(max_length = 254)
	unit = models.ForeignKey(Unit, on_delete = models.CASCADE)
	qty = models.PositiveIntegerField()
	cost = models.FloatField()
	inspection = models.ForeignKey(Inspection, on_delete = models.CASCADE, null = True)
	po_no = models.CharField(max_length = 15, null = True, blank = True)
	acc_code  = models.ForeignKey(AccountCode, on_delete = models.CASCADE, null = True)
	classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null = True)

	def __str__(self):
		return f'{self.desc}'

	@property
	def total(self):
		return self.qty * self.cost

		
class ItemUser(models.Model):
	name = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.name


class ParNumber(models.Model):
	po = models.ForeignKey(PurchaseOrder, on_delete = models.CASCADE, null = True)
	series = models.PositiveIntegerField()
	item_user = models.ForeignKey(ItemUser, on_delete = models.CASCADE)
	date_recorded = models.DateField(default = datetime.datetime.today)

	def __str__(self):
		return f"{self.item_user.name} - {self.par_no}"

	@property
	def par_no(self):
		pad_series = str(self.series).zfill(3)
		y = self.date_recorded.strftime("%y")
		return f"{y}-{pad_series}"

	@property
	def padded_series(self):
		return f"{str(self.series).zfill(3)}"
	

	def max_series(self, recorded_year):
		mx = ParNumber.objects.filter(date_recorded__year = recorded_year).aggregate(Max("series"))['series__max']
		if mx is None:
			return 1
		else:
			return mx + 1

# class NewEndUser(models.Model):
# 	from_par = models.ForeignKey(ParNumber, on_delete = models.CASCADE, null = True, related_name = "from_par")
# 	to_par = models.ForeignKey(ParNumber, on_delete = models.CASCADE, related_name = "to_par")
# 	count = models.PositiveIntegerField(default = 1)
# 	date = models.DateField(default = datetime.datetime.today)


# 	def __str__(self):
# 		return f"{self.from_par.item_user.name} to {self.to_par.item_user.name}"

class InventoryMonitoring(models.Model):
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	balance = models.PositiveIntegerField()
	onhand = models.PositiveIntegerField()
	shortage = models.PositiveIntegerField(default = 0, null = True, blank = True)
	remarks = models.ForeignKey(ItemUser, on_delete = models.CASCADE)
	series = models.PositiveIntegerField()
	wmr = models.CharField(max_length = 15, null = True, blank = True)
	# transferred_to_new_user = models.ForeignKey(NewEndUser, on_delete = models.CASCADE, default=None, null = True, blank = True)
	from_par = models.ForeignKey(ParNumber, on_delete = models.CASCADE, null = True, blank = True, related_name = "from_par")
	designation = models.CharField(max_length = 100, null = True, blank = True)
	date = models.DateTimeField(default = datetime.datetime.now, null = True)
	par_num = models.ForeignKey(ParNumber, on_delete = models.CASCADE, null = True, blank = True, related_name = "par_num")
	equipment_status = models.CharField(max_length = 50, blank = True, null = True)
	user_campus = models.ForeignKey(Campus, on_delete = models.CASCADE)

	@property
	def property_no(self):
		return f'{self.item.acc_code.code}-{str(self.series).zfill(3)}-{self.date.strftime("%m%y")}{self.user_campus.name[0]}'
	
	@property
	def overage(self):
		return self.balance * self.item.cost
	

	def __str__(self):
		return f"{self.property_no} - {self.item.desc}"

	def max_series(self, acc_code):
		mx = InventoryMonitoring.objects.filter(item__acc_code = acc_code).aggregate(Max("series"))['series__max']
		if mx is None:
			return 1
		else:
			return mx + 1

	@property
	def total_val(self):
		return self.balance * self.item.cost

class Level(models.Model):
	name = models.CharField(max_length=  100)

	def __str__(self):
		return self.name

class UserLevel(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	level = models.ForeignKey(Level, on_delete = models.CASCADE)

	@property
	def username(self):
		return self.user.username

	@property
	def first_name(self):
		return self.user.first_name

	@property
	def last_name(self):
		return self.user.last_name
	
	
	
	class Meta:
		verbose_name = "System User"
		verbose_name_plural = "System Users"

	def __str__(self):
		return self.user.username


class ScanModel(models.Model):
	img = models.ImageField(upload_to = "scans")
