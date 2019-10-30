from django import forms
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch,Order_Mens_Or_Ladies,Order_Kids,Order_Ethenic
from bootstrap_modal_forms.forms import BSModalForm

class Update_FabricOrder(BSModalForm):
    class Meta:
        model= Fabric_Order
        fields= ('process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status')
        
class Update_StichingOrder(BSModalForm):
    class Meta:
        model= Stiching
        fields= ('process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status')

class Update_WashingOrder(BSModalForm):
    class Meta:
        model= Washing
        fields= ('process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status')

class Update_FinishingOrder(BSModalForm):
    class Meta:
        model= Finishing
        fields= ('process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status')    
        

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
