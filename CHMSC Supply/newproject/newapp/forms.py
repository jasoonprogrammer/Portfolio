from django import forms
from .models import *
from functools import partial
import datetime
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.helper import FormHelper

def po_no_to_po(po_no):
	try:
		md = po_no.split("-")[0]
		y = po_no.split("-")[2]
		mdy = f'{md}{y}'
		d = datetime.datetime.strptime(mdy, "%m%d%y")
		series = po_no.split("-")[1]
		po = PurchaseOrder.objects.filter(date = d, series = series)
		if po.exists():
			return po.first()
		else:
			return None
	except IndexError:
		return None
	except ValueError:
		return None
	except AttributeError:
		return None
		
class LevelForm(forms.ModelForm):

	class Meta:
		model = UserLevel
		fields = ['level']

class PurchaseOrderForm(forms.Form):
	po_no = forms.CharField(label = "PO No.", help_text = "format xxxx-xxx-xx", widget = forms.TextInput(), )
	date_received_from_bac = forms.DateField(widget = forms.DateInput({'type': 'date'}), label = "Date Received", help_text = "Date received from BAC Office")
	name = forms.CharField(label = "Supplier")
	contact = forms.CharField(label = "Supplier Contact", required = False)
	amounts = forms.FloatField(label = "Amounts", help_text = "Amount shown in Purchase Order")
	fund_source = forms.ModelChoiceField(queryset = FundSource.objects, label="Fund Source")
	mode_of_procurement = forms.ModelChoiceField(queryset = ModeOfProcurement.objects, label = "Mode Of Procurement")
	date_received_by_supplier = forms.DateField(widget =forms.DateInput({'type': 'date'}), label = "Date Receieved By Supplier")
	requesting_end_user_name = forms.CharField(label = "Requesting End User")
	date_received_by_supplier = forms.DateField(widget = forms.DateInput({'type': 'date'}))
	term_of_delivery = forms.IntegerField(label = "Term Of Delivery", help_text = "Number of Days")
	date_to_deliver = forms.DateField(widget = forms.DateInput({'type': 'date', 'readonly': 'readonly'}), help_text = "Auto Generated", required = False)
	remarks = forms.CharField()
	date = forms.DateField(widget = forms.HiddenInput(), required = False)
	series = forms.IntegerField(widget = forms.HiddenInput(), required = False)

	field_order = [
	'po_no',
	'date_received_from_bac',
	'name',
	'contact',
	'amounts',
	'fund_source',
	'mode_of_procurement',
	'date_received_by_supplier',
	'term_of_delivery',
	'date_to_deliver',
	'requesting_end_user_name',
	'date_of_delivery',
	'remarks']

	def clean_po_no(self):
		data = self.cleaned_data['po_no']
		try:
			po_no = data
			md = po_no.split("-")[0]
			series = po_no.split("-")[1]
			y = po_no.split("-")[2]
			if len(series) > 4 or len(series) < 3:
				raise forms.ValidationError("Invalid PO")
			if len(y) != 2:
				raise forms.ValidationError("Invalid PO")
			mdy = f'{md}{y}'
			mdy = datetime.datetime.strptime(mdy, "%m%d%y")
			if PurchaseOrder.objects.filter(date = mdy, series = series).exists():
				return data
			elif PurchaseOrder.objects.filter(date__year = mdy.year, series = series).exists():
				raise forms.ValidationError("This series is already used")
		except IndexError:
			raise forms.ValidationError("Invalid PO")
		return data

	def clean_requesting_end_user_name(self):
		data = self.cleaned_data['requesting_end_user_name']
		while("  " in data):
			data = data.replace("  ", " ")
		data = data.strip()
		data = data.title()
		return data

	def clean_term_of_delivery(self):
		data = self.cleaned_data['term_of_delivery']
		if data < 0:
			raise forms.ValidationError("Please enter positive integer.")
		return data

	def clean_amounts(self):
		data = self.cleaned_data['amounts']
		if data < 0:
			raise forms.ValidationError("Please enter positive integer.")
		return data

	def save(self):
		po = PurchaseOrder()
		po_no = self.cleaned_data['po_no']
		if po_no_to_po(po_no) is not None:
			po = po_no_to_po(po_no)
		po.date = self.cleaned_data['date']
		po.series = self.cleaned_data['series']
		po.date_received_from_bac = self.cleaned_data['date_received_from_bac']
		po.amounts = self.cleaned_data['amounts']
		po.date_received_by_supplier = self.cleaned_data['date_received_by_supplier']
		po.term_of_delivery = self.cleaned_data['term_of_delivery']
		po.remarks = self.cleaned_data['remarks']
		po_no = self.cleaned_data['po_no']
		md = po_no.split("-")[0]
		y = po_no.split("-")[2]
		series = po_no.split("-")[1]
		mdy = f'{md}{y}'
		mdy = datetime.datetime.strptime(mdy, "%m%d%y")
		po.date = mdy
		po.series = series
		po.fund_source = self.cleaned_data['fund_source']
		po.mode_of_procurement =self.cleaned_data['mode_of_procurement']
		reu = RequestingEndUser.objects.create(name = self.cleaned_data['requesting_end_user_name'])
		reu.save()
		po.requesting_end_user = reu
		supplier = Supplier.objects.filter(name = self.cleaned_data['name'])
		if supplier.exists():
			supplier = supplier.first()
			supplier.contact = self.cleaned_data['contact']
		else:
			supplier = Supplier.objects.create(name = self.cleaned_data['name'], contact = self.cleaned_data['contact'])
		po.supplier = supplier
		po.save()
		return po


class InspectionForm(forms.Form):
	po_no = forms.CharField(label = "PO No.", help_text = "format xxxx-xxx-xx", widget = forms.TextInput({'pattern':"(0[1-9]|1[12])([012][0-9]|3[012])-\d{3,4}-\d{2}"}), )
	campus = forms.ModelChoiceField(queryset = Campus.objects)
	inspection_no = forms.CharField(label = "Inspection No.", required = False, widget = forms.TextInput({"readonly": 'readonly'}), help_text = "Autogenerated")
	requisitioning_office = forms.CharField(label = "Requisitioning Office")
	purpose = forms.CharField(label = "Purpose")
	supplier_name = forms.CharField(label = "Supplier")
	date_received = forms.DateField(widget = forms.DateInput({"type": "date"}), label = "Date Received", help_text = "Date Received From Supplier")
	date_inspected = forms.DateField(widget = forms.DateInput({"type": 'date'}), label = "Date Inspected")
	inspection_officer = forms.CharField(label = "Inspection Officer")
	receive_status = forms.ModelChoiceField(widget = forms.RadioSelect, queryset = ReceiveStatus.objects.all(), label = "Receive Status", required = True)

	def clean_po_no(self):
		data = self.cleaned_data['po_no']
		s = data.split('-')
		md = s[0]
		y = s[2]
		try:
			d = datetime.datetime.strptime(f'{md}{y}', "%m%d%y")
			return data
		except ValueError:
			raise forms.ValidationError("Invalid PO No.")


	def clean_date_inspected(self):
		data = self.cleaned_data['date_inspected']
		if data.year < 1900:
			raise forms.ValidationError("Invalid Date, Please date after 1900")
		data = datetime.datetime.combine(data, datetime.time(hour = 0))
		return data

	def save(self):
		s = self.cleaned_data['po_no'].split("-")
		mdy = str(s[0]) + str(s[2])
		po_date = datetime.datetime.strptime(mdy, "%m%d%y")
		series = s[1]
		c_po = PurchaseOrder.objects.filter(date = po_date, series = series)
		r_office = RequisitioningOffice.objects.filter(name = self.cleaned_data['requisitioning_office'])
		if r_office.exists():
			r_office = r_office.first()
		else:
			r_office = RequisitioningOffice.objects.create(name = self.cleaned_data['requisitioning_office'])
		supplier = Supplier.objects.filter(name = self.cleaned_data['supplier_name'])
		if supplier.exists():
			supplier = supplier.first()
		else:
			supplier = Supplier.objects.create(name = self.cleaned_data['supplier_name'])
		print(self.cleaned_data['campus'])
		campus = Campus.objects.filter(name = self.cleaned_data['campus']).first()
		if not c_po.exists():
			c_po = PurchaseOrder.objects.create(date = po_date, series = series)
			c_po.supplier = supplier
			c_po.save()
		else:
			c_po = c_po.first()
		r_status = ReceiveStatus.objects.filter(name = self.cleaned_data['receive_status']).first()
		i_officer = InspectionOfficer.objects.filter(name = self.cleaned_data['inspection_officer'])
		if i_officer.exists():
			i_officer = i_officer.first()
		else:
			i_officer = InspectionOfficer.objects.create(name = self.cleaned_data['inspection_officer'])
		ins = Inspection(po = c_po, requisitioning_office = r_office, campus = campus, date_received = self.cleaned_data['date_received'], 
			date = self.cleaned_data['date_inspected'], receive_status = r_status, inspection_officer = i_officer, purpose = self.cleaned_data['purpose'])
		return ins




class TestForm(forms.Form):
	d = forms.CharField(required = False)


class InventoryFilter(forms.Form):
	po_no = forms.CharField(required = False, label = "PO No.")
	start_date = forms.DateField(widget = forms.DateInput({'type': "date"}), required = False, label = "Start Date")
	end_date = forms.DateField(widget = forms.DateInput({'type': "date"}), required = False, label = "End Date")
	remarks = forms.CharField(required = False)
	article = forms.ModelChoiceField(queryset = Article.objects.all().order_by("name"), required = False)
	campus = forms.ModelChoiceField(queryset = Campus.objects.all().order_by("name"), required = False)
	account_code = forms.ModelChoiceField(queryset = AccountCode.objects.all().order_by("title"), required = False, label = "Account Code")
	value_start = forms.FloatField(required = False, label = "Value Start")
	value_end = forms.FloatField(required = False, label = "Value End")
	end_user_designation = forms.CharField(required = False, label = "User Designation")
	new_end_user = forms.CharField(required = False, label = "Transferred To")

	def clean_po_no(self):
		data = self.cleaned_data['po_no']
		if data == "":
			return None
		po = po_no_to_po(data)
		if po is None:
			raise forms.ValidationError("PO Not Found")
		return data

	def search(self):
		objs = InventoryMonitoring.objects.all()
		if self.cleaned_data['start_date'] is not None:
			objs = objs.filter(date__gte = self.cleaned_data['start_date'])
		if self.cleaned_data['end_date'] is not None:
			objs = objs.filter(date__lte = self.cleaned_data['end_date'])
		if self.cleaned_data['remarks'] != "":
			objs = objs.filter(remarks__name__icontains = self.cleaned_data['remarks'])
		if self.cleaned_data['article'] is not None:
			objs = objs.filter(item__article = self.cleaned_data['article'])
		if self.cleaned_data['account_code'] is not None:
			objs = objs.filter(item__acc_code = self.cleaned_data['account_code'])
		if self.cleaned_data['value_start'] is not None:
			objs = objs.filter(item__cost__gte = self.cleaned_data['value_start'])
		if self.cleaned_data['value_end'] is not None:
			objs = objs.filter(item__cost__lte = self.cleaned_data['value_end'])
		po = po_no_to_po(self.cleaned_data['po_no'])
		if po is not None:
			objs = objs.filter(item__inspection__po = po)
		if self.cleaned_data['end_user_designation'] != "":
			d = self.cleaned_data['end_user_designation']
			objs = objs.filter(designation__icontains =d)
		if self.cleaned_data['new_end_user'] != "":
			objs = objs.filter(transferred_to_new_user__name = self.cleaned_data['new_end_user'])
		if self.cleaned_data['campus'] is not None:
			objs = objs.filter(user_campus = self.cleaned_data['campus'])
		return objs


class POFilter(forms.Form):
	start_date = forms.DateField(widget = forms.DateInput({'type': "date"}), required = False, label = "Start Date")
	end_date = forms.DateField(widget = forms.DateInput({'type': "date"}), required = False, label = "End Date")
	supplier = forms.CharField(required = False, label = "Supplier Name")
	amounts_start = forms.FloatField(widget = forms.TextInput({"type": "number"}), required = False, label = "Amounts Start")
	amounts_end = forms.FloatField(widget = forms.TextInput({"type": "number"}), required = False, label = "Amounts End")
	fund_source = forms.ModelChoiceField(required = False, queryset = FundSource.objects.all(), label = "Fund Source")
	mode_of_procurement = forms.ModelChoiceField(required = False, queryset = ModeOfProcurement.objects.all(), label = "Mode of Procurement")
	requesting_user = forms.CharField(required = False, label = "Requesting User")

	def search(self):
		objs = PurchaseOrder.objects.all()
		if self.cleaned_data['start_date'] is not None:
			objs = objs.filter(date__gte = self.cleaned_data['start_date'])
		if self.cleaned_data['end_date'] is not None:
			objs = objs.filter(date__lte = self.cleaned_data['end_date'])
		if self.cleaned_data['amounts_start'] is not None:
			objs = objs.filter(amounts__gte = self.cleaned_data['amounts_start'])
		if self.cleaned_data['amounts_end'] is not None:
			objs = objs.filter(amounts__lte = self.cleaned_data['amounts_end'])
		if self.cleaned_data['supplier'] != "":
			objs = objs.filter(supplier__name__icontains = self.cleaned_data['supplier'])
		if self.cleaned_data['fund_source'] is not None:
			objs = objs.filter(fund_source = self.cleaned_data['fund_source'])
		if self.cleaned_data['mode_of_procurement'] is not None:
			objs = objs.filter(mode_of_procurement = self.cleaned_data['mode_of_procurement'])
		if self.cleaned_data['requesting_user'] != "":
			objs = objs.filter(requesting_end_user__name__icontains = self.cleaned_data['requesting_user'])

		return objs

class Scanner(forms.ModelForm):
	img = forms.FileField(label = "")
	class Meta:
		model = ScanModel
		fields = "__all__"


class InspectionUpdateForm(forms.Form):
	id = forms.CharField(label = "", widget = forms.HiddenInput({"type": "hidden"}))
	requisitioning_office = forms.CharField(label = "Requisitioning Office")
	campus = forms.ModelChoiceField(queryset = Campus.objects.all(), label = "Campus")
	receive_status = forms.ModelChoiceField(queryset = ReceiveStatus.objects.all(), label = "Receive Status")
	date_inspected = forms.DateField(widget = forms.DateInput({"type": "date"}), label = "Date Inspected")
	date_received = forms.DateField(widget = forms.DateInput({"type": "date"}), label = "Date Received")
	supplier_name = forms.CharField(label = "Supplier")

	def save(self):
		ins = Inspection.objects.get(pk = self.cleaned_data['id'])
		if RequisitioningOffice.objects.filter(name = self.cleaned_data['requisitioning_office']).exists():
			new_ro = RequisitioningOffice.objects.filter(name = self.cleaned_data['requisitioning_office']).first()
		else:
			new_ro = RequisitioningOffice(name = self.cleaned_data['requisitioning_office'])
			new_ro.save()
		ins.requisitioning_office = new_ro
		ins.supplier = Supplier.objects.filter(name = self.cleaned_data['supplier_name']).first() or Supplier.objects.create(name = self.cleaned_data['supplier_name'])
		ins.campus = self.cleaned_data['campus']
		ins.receive_status = self.cleaned_data['receive_status']
		ins.date_inspected = self.cleaned_data['date_inspected']
		ins.date_received = self.cleaned_data['date_received']
		ins.save()
		return ins

class POEncodingForm(forms.ModelForm):

    date = forms.DateField(widget = forms.DateInput({"type": "date"}), required = False, label = "PO Date")
    supplier = forms.CharField()
    requesting_end_user = forms.CharField()
    date_received_by_supplier = forms.DateField(widget = forms.DateInput({"type": "date"}), required = False)
    date_received_from_bac = forms.DateField(widget = forms.DateInput({"type": "date"}), required = False)
    date_recorded = forms.DateField(widget = forms.DateInput({"type": "date"}), required = False)
    remarks = forms.CharField(required = False)

    class Meta:
    	model = PurchaseOrder
    	fields = "__all__"



    def clean_supplier(self, *args, **kwags):
    	data = self.cleaned_data.get("supplier")
    	all_supplier_name = [x.name for x in Supplier.objects.all()]
    	if data in all_supplier_name:
    		return Supplier.objects.filter(name = data).first()
    	else:
    		return Supplier.objects.create(name = data)

    def clean_requesting_end_user(self, *args, **kwargs):
    	data = self.cleaned_data.get("requesting_end_user")
    	all_user_name = [x.name for x in RequestingEndUser.objects.all()]
    	if data in all_user_name:
    		return RequestingEndUser.objects.filter(name = data).first()
    	else:
    		return RequestingEndUser.objects.create(name = data)

    field_order = [
    	'date',
    	'series',
    	'mode_of_procurement',
    	'supplier',
    	'term_of_delivery',
    	'purpose',
    	'requesting_end_user',
    	'fund_source',
    	'amounts',
    	'date_received_by_supplier',
    	'date_received_from_bac',
    	'remarks']


class InspectionEncodingForm(forms.ModelForm):
	series = forms.IntegerField(required = False)
	date = forms.DateField(widget = forms.DateInput({"type": "date"}), label = "Inspection Date")
	purpose = forms.CharField()
	po = forms.CharField(label = "PO No.", widget = forms.TextInput({'pattern':"(0[1-9]|1[12])([012][0-9]|3[012])-\d{3,4}-\d{2}"}))
	requisitioning_office = forms.CharField()
	date_received = forms.DateField(widget = forms.DateInput({"type": "date"}))
	inspection_officer = forms.CharField()
	inspection_date = forms.DateField(widget = forms.DateInput({"type": "date"}))

	class Meta:
		model = Inspection
		exclude = ("with_acc_codes", )



	def clean_po(self, *args, **kwargs):
		data = self.cleaned_data.get("po")
		all_po = [x.po_no for x in PurchaseOrder.objects.all()]
		if data in all_po:
			po = [x for x in PurchaseOrder.objects.all() if x.po_no == data] 
			return po[0]
		else:
			md = po_no.split("-")[0]
			y = po_no.split("-")[2]
			mdy = f'{md}{y}'
			d = datetime.datetime.strptime(mdy, "%m%d%y")
			series = po_no.split("-")[1]
			po = PurchaseOrder(date = d, series = series)
			po = po.save()
			return po

	def clean_requisitioning_office(self, *args, **kwargs):
		data = self.cleaned_data.get("requisitioning_office")
		all_office = [x.name for x in RequisitioningOffice.objects.all()]
		if data in all_office:
			return RequisitioningOffice.objects.filter(name = data).first()
		else:
			return RequisitioningOffice.objects.create(name = data)

	def clean_inspection_officer(self, *args, **kwargs):
		data = self.cleaned_data.get("inspection_officer")
		all_inspectors = [x.name for x in InspectionOfficer.objects.all()]
		if data in all_inspectors:
			return InspectionOfficer.objects.filter(name = data).first()
		else:
			return InspectionOfficer.objects.create(name = data)

	field_order = [
	'date',
	'series',
	'po',
	'requisitioning_office',
	'purpose',
	]


class ItemEncodingForm(forms.ModelForm):

	article = forms.CharField()
	inspection = forms.CharField(widget = forms.TextInput({"class": "inspection_input"}))
	acc_code = forms.CharField()

	class Meta:
		model = Item
		fields = "__all__"

	def clean_article(self, *args, **kwargs):
		data = self.cleaned_data.get("article")
		all_article = [x.name for x in Article.objects.all()]
		if data in all_article:
			return Article.objects.filter(name = data).first()
		else:
			return Article.objects.create(name = data)

	def clean_acc_code(self, *args, **kwargs):
		data = self.cleaned_data.get("acc_code")
		all_codes = [x.code for x in AccountCode.objects.all()]
		if data in all_codes:
			return AccountCode.objects.filter(code = data).first()
		else:
			return AccountCode.objects.create(code = data, title = "")

	def clean_inspection(self, *args, **kwargs):
		data = self.cleaned_data.get("inspection")
		all_inspection = [x.ins_no for x in Inspection.objects.all()]
		if data in all_inspection:
			return [x for x in Inspection.objects.all() if x == x.ins_no][0]
		elif data == "":
			return None
		else:
			raise forms.ValidationError("Invalid Inspection No")


class AccountCodeForm(forms.ModelForm):

	class Meta:
		model = AccountCode
		fields = "__all__"

class InventoryEncodingForm(forms.ModelForm):

	class Meta:
		model = InventoryMonitoring
		fields = "__all__"

class ReceiptEncodingForm(forms.ModelForm):
	type = forms.ModelChoiceField(queryset = ReceiptType.objects, label="Receipt Type")
	no = forms.CharField(label = "Receipt No.")
	date = forms.DateField(widget = forms.DateInput({"type": "date"}), label = "Receipt Date")
	inspection = forms.CharField(widget = forms.TextInput({"type": "hidden"}), required = False)

	class Meta:
		model = Receipt
		fields = "__all__"