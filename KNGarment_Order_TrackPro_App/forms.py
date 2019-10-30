from django import forms
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch,Order_Mens_Or_Ladies,Order_Kids,Order_Ethenic
from bootstrap_modal_forms.forms import BSModalForm

class Update_FabricOrder(BSModalForm):
    class Meta:
        model= Fabric_Order
        fields= ('process_vendor_name',
        'process_vendor_location',
        'process_received_quantity',
        'process_received_date',
        'process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status',
        'fabric_order_sort_number',
        'fabric_order_quantity')
        
class Update_StichingOrder(BSModalForm):
    class Meta:
        model= Stiching
        fields= ('process_vendor_name',
        'process_vendor_location',
        'process_received_quantity',
        'process_received_date',
        'process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status',
        'stiching_average_one',
        'stiching_average_two',
        'stiching_average_three',
        'stiching_rate_one',
        'stiching_rate_two',
        'stiching_rate_three',
        'stiching_opening_fabric_stock',
        'stiching_opening_stock_date',
        'stiching_fabric_bill_date',
        'stiching_fabric_used',
        'stiching_fabric_bill_number')

class Update_WashingOrder(BSModalForm):
    class Meta:
        model= Washing
        fields= ('process_vendor_name',
        'process_vendor_location',
        'process_received_quantity',
        'process_received_date',
        'process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status',
        'washing_process_name',
        'washing_rate',
        'washing_order_date',
        'washing_delivery_quantity')

class Update_FinishingOrder(BSModalForm):
    class Meta:
        model= Finishing
        fields= ('process_vendor_name',
        'process_vendor_location',
        'process_received_quantity',
        'process_received_date',
        'process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status',
        'finishing_rate',
        'finishing_delivery_quantity')     
        

class Update_DispatchOrder(BSModalForm):
    class Meta:
        model= Dispatch
        fields= ('dispatch_received_quantity',
        'dispatch_received_date',
        'dispatch_dispatch_quantity',
        'dispatch_balance_quantity',
        'dispatch_rejected_quantity',
        'dispatch_bill_number',
        'dispatch_bill_file',
        'dispatch_payment_status')    
