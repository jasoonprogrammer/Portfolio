from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
admin.site.register(RequisitioningOffice)
admin.site.register(Inspection)
admin.site.register(InspectionOfficer)
admin.site.register(Campus)
admin.site.register(Receipt)
admin.site.register(ReceiptType)
admin.site.register(AccountCode)
admin.site.register(InventoryMonitoring)
# admin.site.register(NewEndUser)
admin.site.register(Level)
admin.site.register(ScanModel)
admin.site.register(Supplier)
admin.site.register(ParNumber)
admin.site.register(Article)






@admin.register(UserLevel)
class UserLevelAdmin(admin.ModelAdmin):
	list_display = ['username', 'first_name', 'last_name', 'level']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'po_no', 'date', 'supplier_name', 'amounts', 'date_to_deliver']

@admin.register(ItemUser)
class ItemUserAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ['desc', 'inspection', 'cost', "qty"]

