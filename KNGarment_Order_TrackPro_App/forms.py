from django import forms
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch,Order_Mens_Or_Ladies,Order_Kids,Order_Ethenic,CustomUser
from bootstrap_modal_forms.forms import BSModalForm

class CustomUserForm(BSModalForm):
    class Meta:
        model = CustomUser
        fields = ['user_role','username','email']

class Update_Orders(BSModalForm):
    class Meta:
        model = Orders
        fields = ('order_order_number',
        'order_order_type',
        'order_order_brands',
        'order_order_style_number',
        'order_order_fit',
        'order_order_quantity',
        'order_order_date',
        'order_delivery_date',
        'order_order_category',
        'order_fit_sample_submitted_date',
        'order_pps_sample_submitted_date',
        'order_order_remark')
        
class Update_FabricOrderProcess(BSModalForm):
    class Meta:
        model = Fabric_Order
        fields = ('fabric_order_sort_number',
        'fabric_order_quantity',
        'process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status')

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

class Update_Process_payment_status(BSModalForm):
    class Meta:
        model= Process
        fields= ('process_payment_status',)