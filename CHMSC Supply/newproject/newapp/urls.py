from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('home', views.HomeView.as_view(), name = 'home'),
	path('logout', auth_views.LogoutView.as_view(template_name = 'newapp/logout.html'), name="logout"),
	path('po_monitoring', views.po_monitoring, name = "po_monitoring"),
	path('new', views.new, name = "new"),
	path("get_contact", views.get_contact, name = 'get_contact'),
	path("inspection_form", views.inspection_form, name = 'inspection_form'),
	path("none", views.none, name = "none"),
	path("none2", views.none2, name = "none2"),
	path("receipt_row", views.receipt_row, name = "receipt_row"),
	path("generate_inspection_no", views.generate_inspection_no, name = 'generate_inspection_no'),
	path("item-row", views.item_row, name = "item-row"),
	path("set-acc-codes-list", views.set_account_codes_list, name='acc_code_list'),
	path("acc-codes-ins/<int:pk>", views.set_account_codes_ins, name='acc-codes-ins'),
	path("get-acc-info", views.get_acc_info, name = "get-acc-info"),
	path("get-acc-info-2", views.get_acc_info2, name = "get-acc-info-2"),
	path("inventory-monitoring-form", views.inventory_monitoring_form, name = "inventory-monitoring-form"),
	path("monitoring-row-form", views.monitoring_row_form, name = "monitoring-row-form"),
	path("property-tag", views.get_property_tag, name = 'property-tag'),
	path("ins-po", views.ins_po, name = 'ins-po'),
	path("po-list", views.po_list, name = "po-list"),
	path("inventory-list", views.inventory_list, name = "inventory-list"),
	path('inventory/tag/<int:pk>', views.sticker, name = "sticker"),
	path('scan', views.scan, name = "scan"),
	path("info/<int:pk>", views.info, name = "info"),
	path("print/inspection/<int:ins_no>", views.print_ins, name="print-ins"),
	path("list/inspection", views.InspectionListView.as_view(), name = "inspection-list"),
	path("update/inspection/<int:pk>", views.update_inspection, name = "update-inspection"),
	path("print/par", views.print_par, name = "print-par"),
	path("print/inv", views.print_inventory, name = "print-inv"),
	path("delete/inspection/<int:pk>", views.delete_inspection, name = "delete-inspection"),
	path("po_list_option", views.change_options, name="po_list_option"),
	path("print_ics", views.print_ics, name = "print-ics"),
	path("transfer_items", views.transfer_items, name="transfer-items"),
	path("confirm_transfer", views.confirm_transfer, name = "confirm-transfer"),
	path("name_transfer_autocheck", views.name_transfer_autocheck, name="name-transfer-autocheck"),
	path("property_timeline/<slug:property_no>", views.property_timeline, name="property-timeline"),
	path("par_list", views.par_list, name="par_list"),
	path("accounting", views.accounting, name="accounting"),


	path("encoding/po", views.POEncodingView.as_view(), name="po_encoding"),
	path("encoding/inspection", views.InspectionEncodingView.as_view(), name="inspection_encoding"),
	path("encoding/item", views.ItemEncodingView.as_view(), name="item_encoding"),
	path('encoding/item_formset', views.ItemEncodingFormsetView.as_view(), name="item_encoding_formset"),
	path("encoding/delete-po>", views.delete_po, name="delete-po")



]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)