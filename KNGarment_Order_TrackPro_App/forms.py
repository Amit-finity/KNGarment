from django import forms
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch,Order_Mens_Or_Ladies,Order_Kids,Order_Ethenic,CustomUser
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

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

class Update_StichingOrderProcess(BSModalForm):
    class Meta:
        model = Stiching
        fields = ('stiching_average_one',
        'stiching_average_two',
        'stiching_average_three',
        'stiching_rate_one',
        'stiching_rate_two',
        'stiching_rate_three',
        'stiching_opening_fabric_stock',
        'stiching_opening_stock_date',
        'stiching_fabric_bill_date',
        'stiching_fabric_used',
        'stiching_fabric_bill_number',
        'process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status')

class Update_WashingOrderProcess(BSModalForm):
    class Meta:
        model = Washing
        fields = ('washing_process_name',
        'washing_rate',
        'washing_order_date',
        'process_vendor_name',
        'process_vendor_location',
        'process_delivery_date',
        'process_bill_number',
        'process_bill_file',
        'process_payment_status')
        
class Update_FinishingOrderProcess(BSModalForm):
    class Meta:
        model = Finishing
        fields = ('finishing_rate',
        'finishing_delivery_quantity',
        'process_vendor_name',
        'process_vendor_location',
        'process_received_quantity',
        'process_received_date',
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

class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['user_role','email','username', 'password1', 'password2']