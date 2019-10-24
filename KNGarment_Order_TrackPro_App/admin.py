from django.contrib import admin
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "client_name",
    ]

class VendorAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "vendor_name",
        "vendor_type",
    ]

class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "order_order_number",
        "order_order_type",
    ]

class ProcessAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "process_vendor_name",
        "process_vendor_location",
    ]

class FabricOrderAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "fabric_order_sort_number",
        "fabric_order_quantity",
    ]

class StichingAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "stiching_fabric_bill_date",
        "stiching_fabric_used",
    ]

class WashingAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "washing_process_name",
        "washing_rate",
        "washing_order_date",
    ]

class FinishingAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "finishing_rate",
        "finishing_delivery_quantity",
    ]

class DispatchAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "dispatch_bill_number",
        "dispatch_received_quantity",
        "dispatch_received_date",
        "dispatch_dispatch_quantity",
        "dispatch_balance_quantity",
        "dispatch_rejected_quantity",
    ]



admin.site.register(Client,ClientAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Process,ProcessAdmin)
admin.site.register(Fabric_Order,FabricOrderAdmin)
admin.site.register(Stiching,StichingAdmin)
admin.site.register(Washing,WashingAdmin)
admin.site.register(Finishing,FinishingAdmin)
admin.site.register(Dispatch,DispatchAdmin)