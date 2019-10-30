#External Imports
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.utils import timezone

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
#import json
#from django.contrib.auth.hashers import make_password
#from django.core.mail import send_mail
from bootstrap_modal_forms.generic import (BSModalCreateView,BSModalUpdateView,BSModalReadView,BSModalDeleteView)

#Project Imports
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch,Order_Mens_Or_Ladies,Order_Kids,Order_Ethenic
from KNGarment_Order_TrackPro_App.forms import Update_FabricOrder,Update_StichingOrder,Update_WashingOrder,Update_FinishingOrder,Update_DispatchOrder,Update_Process_payment_status 

# Create your views here.

def add_new_order_form(request):
    return render(request,'KNGarment_Order_TrackPro_App/Add_orders.html')

def update_order_detail(request):
    orders = Orders.objects.all()
    data = {'orders':orders}
    return render(request,'KNGarment_Order_TrackPro_App/update_orders_detail.html',data)


def add_processes(request,pk):
    fabric_bill_numbers = Fabric_Order.objects.all()
    order_object = Orders.objects.get(pk=pk)
    order_mens_or_ladies_object = Order_Mens_Or_Ladies.objects.get(order_mens_or_ladies_order_id=pk)
    order_kids_object = Order_Kids.objects.get(order_kids_order_id=pk)
    order_ethenic_object = Order_Ethenic.objects.get(order_ethenic_order_id=pk)
    data = {'orders':order_object,
            'fabric_bill_numbers':fabric_bill_numbers,
            'order_mens_or_ladies':order_mens_or_ladies_object,
            'order_kids':order_kids_object,
            'order_ethenic':order_ethenic_object}
    return render(request,'KNGarment_Order_TrackPro_App/add_processes.html',data)

def current_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Current.html')

def delivered_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/delivered_orders.html')

def track_order_registered_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Order_registered.html')

def track_order_details(request,pk):
    fabric_bill_numbers = Fabric_Order.objects.all()
    fabric_object = Fabric_Order.objects.get(process_order_id=pk)
    stiching_object = Stiching.objects.get(process_order_id=pk)
    washing_object = Washing.objects.get(process_order_id=pk)
    finishing_object = Finishing.objects.get(process_order_id=pk)
    dispatch_object = Dispatch.objects.latest('dispatch_order_date_of_entry')
    order_object = Orders.objects.get(pk=pk)
    order_mens_or_ladies_object = Order_Mens_Or_Ladies.objects.get(order_mens_or_ladies_order_id=pk)
    order_kids_object = Order_Kids.objects.get(order_kids_order_id=pk)
    order_ethenic_object = Order_Ethenic.objects.get(order_ethenic_order_id=pk)
    data = {'orders':order_object,
            'fabric_bill_numbers':fabric_bill_numbers,
            'order_mens_or_ladies':order_mens_or_ladies_object,
            'order_kids':order_kids_object,
            'order_ethenic':order_ethenic_object,
            'fabric':fabric_object,
            'stiching':stiching_object,
            'washing':washing_object,
            'finishing':finishing_object,
            'dispatch':dispatch_object}
    return render(request,'KNGarment_Order_TrackPro_App/Order_Details_2.html',data)

def track_order_fabric_order(request):
    fabric_order_objects = Fabric_Order.objects.all()
    data = {'fabric_order':fabric_order_objects}
    return render(request,'KNGarment_Order_TrackPro_App/fabric_order.html',data)



def track_order_stiching_order(request):
    stiching_order_objects = Stiching.objects.all()
    data = {'stiching_order':stiching_order_objects}
    return render(request,'KNGarment_Order_TrackPro_App/stiching.html',data)

def track_order_washing_order(request):
    washing_order_objects = Washing.objects.all()
    data = {'washing_order':washing_order_objects}
    return render(request,'KNGarment_Order_TrackPro_App/Washing.html',data)

def track_order_finishing_order(request):
    finishing_order_objects = Finishing.objects.all()
    data = {'finishing_order':finishing_order_objects}
    return render(request,'KNGarment_Order_TrackPro_App/Finishing.html',data)

def track_order_dispatched_order(request):
    dispatch_order_objects = Dispatch.objects.all()
    data = {'dispatch_order':dispatch_order_objects}
    return render(request,'KNGarment_Order_TrackPro_App/dispatch.html',data)

def payment_pending(request):
    process_objects = Process.objects.all().filter(process_payment_status=2)
    data = {'processes':process_objects}
    return render(request,'KNGarment_Order_TrackPro_App/pending_order.html',data)

def payment_paid(request):
    process_objects = Process.objects.all().filter(process_payment_status=1)
    data = {'processes':process_objects}
    return render(request,'KNGarment_Order_TrackPro_App/paid_order.html',data)

def reports_job_worker_balancereport(request):
    return render(request,'KNGarment_Order_TrackPro_App/job_worker_bal_report.html')

def reports_stockreport(request):
    return render(request,'KNGarment_Order_TrackPro_App/stock_report.html')

def track_order_production_details(request):
    return render(request,'KNGarment_Order_TrackPro_App/Production.html')

def report_error(request):
    return render(request,'KNGarment_Order_TrackPro_App/report_error.html')

def forget_password(request):
    return render(request,'KNGarment_Order_TrackPro_App/forget_password.html')

def user_login(request):
    return render(request,'KNGarment_Order_TrackPro_App/login_form.html')

def register(request):
    return render(request,'KNGarment_Order_TrackPro_App/register_form.html')

# Logout
def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:user_login'))

def add_new_order_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        order_order_number = request.POST['order_order_number']
        order_order_type = request.POST['order_order_type']
        order_order_brands = request.POST['order_order_brands']
        order_order_style_number = request.POST['order_order_style_number']
        order_order_fit = request.POST['order_order_fit']
        order_order_quantity = request.POST['order_order_quantity']
        order_order_date = request.POST['order_order_date']
        order_delivery_date = request.POST['order_delivery_date']
        order_order_category = request.POST['order_order_category']
        order_order_remark = request.POST['order_order_remark']
        order_object = Orders.objects.create(order_order_number = order_order_number,
                                        order_order_type = order_order_type,
                                        order_order_brands = order_order_brands,
                                        order_order_style_number = order_order_style_number,
                                        order_order_fit = order_order_fit,
                                        order_order_quantity = order_order_quantity,
                                        order_order_date = order_order_date,
                                        order_delivery_date = order_delivery_date,
                                        order_order_category = order_order_category,
                                        order_order_remark = order_order_remark,
                                        order_client_id = Client.objects.latest('pk'))
        orders_latest_object = Orders.objects.latest('order_order_date_of_entry') 

        if request.POST.get('mens_or_ladies_checkbox', False) == 'mensorladies':            
            quantity_26 = request.POST['quantity_26']
            quantity_28 = request.POST['quantity_28']
            quantity_30 = request.POST['quantity_30']
            quantity_32 = request.POST['quantity_32']
            quantity_34 = request.POST['quantity_34']
            quantity_36 = request.POST['quantity_36']
            quantity_38 = request.POST['quantity_38']
            quantity_40 = request.POST['quantity_40']
            quantity_42 = request.POST['quantity_42']
            quantity_44 = request.POST['quantity_44']

            Order_Mens_Or_Ladies.objects.create(order_mens_or_ladies_size_26_quantity = quantity_26,
            order_mens_or_ladies_size_28_quantity = quantity_28,
            order_mens_or_ladies_size_30_quantity = quantity_30,
            order_mens_or_ladies_size_32_quantity = quantity_32,
            order_mens_or_ladies_size_34_quantity = quantity_34,
            order_mens_or_ladies_size_36_quantity = quantity_36,
            order_mens_or_ladies_size_38_quantity = quantity_38,
            order_mens_or_ladies_size_40_quantity = quantity_40,
            order_mens_or_ladies_size_42_quantity = quantity_42,
            order_mens_or_ladies_size_44_quantity = quantity_44,
            order_mens_or_ladies_order_id = Orders.objects.latest('order_order_date_of_entry'))
        
        if request.POST.get('kids_checkbox', False) == 'kids': 
            order_kids_age_2_years = request.POST['2_years']
            order_kids_age_3to4_years = request.POST['3_4_years']
            order_kids_age_5to6_years = request.POST['5_6_years']
            order_kids_age_7to8_years = request.POST['7_8_years']
            order_kids_age_9to10_years = request.POST['9_10_years']
            order_kids_age_11to12_years = request.POST['11_12_years']
            order_kids_age_13to14_years = request.POST['13_14_years']
            order_kids_age_15to16_years = request.POST['15_16_years']
            order_kids_age_2to3_years = request.POST['2_3_years']
            order_kids_age_4to5_years = request.POST['4_5_years']
            order_kids_age_6to7_years = request.POST['6_7_years']
            order_kids_age_8to9_years = request.POST['8_9_years']
            order_kids_age_10to11_years = request.POST['10_11_years']

            Order_Kids.objects.create(order_kids_age_2_years = order_kids_age_2_years,
            order_kids_age_3to4_years = order_kids_age_3to4_years,
            order_kids_age_5to6_years = order_kids_age_5to6_years,
            order_kids_age_7to8_years = order_kids_age_7to8_years,
            order_kids_age_9to10_years = order_kids_age_9to10_years,
            order_kids_age_11to12_years = order_kids_age_11to12_years,
            order_kids_age_13to14_years = order_kids_age_13to14_years,
            order_kids_age_15to16_years = order_kids_age_15to16_years,
            order_kids_age_2to3_years = order_kids_age_2to3_years,
            order_kids_age_4to5_years = order_kids_age_4to5_years,
            order_kids_age_6to7_years = order_kids_age_6to7_years,
            order_kids_age_8to9_years = order_kids_age_8to9_years,
            order_kids_age_10to11_years = order_kids_age_10to11_years,
            order_kids_order_id = Orders.objects.latest('order_order_date_of_entry'))

        if request.POST.get('ethenic_checkbox', False) == 'ethenic':
            order_ethenic_size_XS = request.POST['xs_size']
            order_ethenic_size_S = request.POST['s_size']
            order_ethenic_size_M = request.POST['m_size']
            order_ethenic_size_L = request.POST['l_size']
            order_ethenic_size_XL = request.POST['xl_size']
            order_ethenic_size_XXL = request.POST['xxl_size']
            order_ethenic_size_XXXL = request.POST['xxxl_size']

            Order_Ethenic.objects.create(order_ethenic_size_XS = order_ethenic_size_XS,
            order_ethenic_size_S = order_ethenic_size_S,
            order_ethenic_size_M = order_ethenic_size_M,
            order_ethenic_size_L = order_ethenic_size_L,
            order_ethenic_size_XL = order_ethenic_size_XL,
            order_ethenic_size_XXL = order_ethenic_size_XXL,
            order_ethenic_size_XXXL = order_ethenic_size_XXXL,
            order_ethenic_order_id = Orders.objects.latest('order_order_date_of_entry'))

    return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_processes',kwargs={'pk': orders_latest_object.pk}))


def add_new_fabric_order_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        fabric_order_sort_number = request.POST['fabric_order_sort_number']
        process_vendor_name = request.POST['process_vendor_name']
        process_received_quantity = request.POST['process_received_quantity']
        process_delivery_date = request.POST['process_delivery_date']
        Fabric_Order.objects.create(fabric_order_sort_number = fabric_order_sort_number,
                                        process_vendor_name = process_vendor_name,
                                        process_received_quantity = process_received_quantity,
                                        process_delivery_date = process_delivery_date,
                                        process_vendor_id=Vendor.objects.latest('pk'),
                                        process_order_id=Orders.objects.latest('pk'))
        Order_object = Orders.objects.latest('order_order_date_of_entry')
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:track_order_details',kwargs={'pk': Order_object.pk}))

def add_new_stiching_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        process_vendor_name = request.POST['process_vendor_name']
        process_vendor_location = request.POST['process_vendor_location']
        stiching_average_one = request.POST['stiching_average_one']
        stiching_average_two = request.POST['stiching_average_two']
        stiching_average_three = request.POST['stiching_average_three']
        stiching_rate_one = request.POST['stiching_rate_one']
        stiching_rate_two = request.POST['stiching_rate_two']
        stiching_rate_three = request.POST['stiching_rate_three']
        process_delivery_date = request.POST['process_delivery_date']
        stiching_opening_fabric_stock = request.POST['stiching_opening_fabric_stock']
        stiching_opening_stock_date = request.POST['stiching_opening_stock_date']
        process_received_date = request.POST['process_received_date']
        stiching_fabric_bill_number = request.POST['stiching_fabric_bill_number']
        stiching_fabric_bill_date = request.POST['stiching_fabric_bill_date']
        process_received_quantity = request.POST['process_received_quantity']
        stiching_fabric_used = request.POST['stiching_fabric_used']
        stiching_fabric_bill_number = request.POST['stiching_fabric_bill_number']
        process_bill_file = request.POST['process_bill_file']
        Stiching.objects.create(process_vendor_name = process_vendor_name,
                                        process_vendor_location = process_vendor_location,
                                        stiching_average_one = stiching_average_one,
                                        stiching_average_two = stiching_average_two,
                                        stiching_average_three=stiching_average_three,
                                        stiching_rate_one=stiching_rate_one,
                                        stiching_rate_two = stiching_rate_two,
                                        stiching_rate_three=stiching_rate_three,
                                        process_delivery_date=process_delivery_date,
                                        stiching_opening_fabric_stock=stiching_opening_fabric_stock,
                                        stiching_opening_stock_date=stiching_opening_stock_date,
                                        process_received_date=process_received_date,
                                        stiching_fabric_bill_date=stiching_fabric_bill_date,
                                        process_received_quantity=process_received_quantity,
                                        stiching_fabric_used=stiching_fabric_used,
                                        stiching_fabric_bill_number=stiching_fabric_bill_number,
                                        process_bill_file=process_bill_file,
                                        process_vendor_id=Vendor.objects.latest('pk'),
                                        process_order_id=Orders.objects.latest('pk'))
        Order_object = Orders.objects.latest('order_order_date_of_entry')
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:track_order_details',kwargs={'pk': Order_object.pk}))

def add_new_washing_order_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        process_vendor_name = request.POST['process_vendor_name']
        process_vendor_location = request.POST['process_vendor_location']
        process_received_quantity = request.POST['process_received_quantity']
        process_received_date = request.POST['process_received_date']
        washing_process_name = request.POST['washing_process_name']
        washing_rate = request.POST['washing_rate']
        process_delivery_date = request.POST['process_delivery_date']
        washing_delivery_quantity = request.POST['washing_delivery_quantity']
        process_bill_number = request.POST['process_bill_number']
        process_bill_file = request.POST['process_bill_file']
        Washing.objects.create(process_vendor_name = process_vendor_name,
                                        process_vendor_location = process_vendor_location,
                                        process_received_quantity = process_received_quantity,
                                        process_received_date = process_received_date,
                                        washing_process_name = washing_process_name,
                                        washing_rate = washing_rate,
                                        process_delivery_date = process_delivery_date,
                                        washing_delivery_quantity = washing_delivery_quantity,
                                        process_bill_number = process_bill_number,
                                        process_bill_file = process_bill_file,
                                        process_vendor_id=Vendor.objects.latest('pk'),
                                        process_order_id=Orders.objects.latest('pk'))
        Order_object = Orders.objects.latest('order_order_date_of_entry')
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:track_order_details',kwargs={'pk': Order_object.pk}))

def add_new_finishing_order_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        process_vendor_name = request.POST['process_vendor_name']
        process_vendor_location = request.POST['process_vendor_location']
        process_received_quantity = request.POST['process_received_quantity']
        process_received_date = request.POST['process_received_date']
        finishing_rate = request.POST['finishing_rate']
        process_delivery_date = request.POST['process_delivery_date']
        finishing_delivery_quantity = request.POST['finishing_delivery_quantity']
        process_bill_number = request.POST['process_bill_number']
        process_bill_file = request.POST['process_bill_file']
        Finishing.objects.create(process_vendor_name = process_vendor_name,
                                        process_vendor_location = process_vendor_location,
                                        process_received_quantity = process_received_quantity,
                                        process_received_date = process_received_date,
                                        finishing_rate = finishing_rate,
                                        process_delivery_date = process_delivery_date,
                                        finishing_delivery_quantity = finishing_delivery_quantity,
                                        process_bill_number = process_bill_number,
                                        process_bill_file = process_bill_file,
                                        process_vendor_id=Vendor.objects.latest('pk'),
                                        process_order_id=Orders.objects.latest('pk'))
        Order_object = Orders.objects.latest('order_order_date_of_entry')
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:track_order_details',kwargs={'pk': Order_object.pk}))

def add_new_dispatch_order_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        dispatch_received_quantity = request.POST['dispatch_received_quantity']
        dispatch_received_date = request.POST['dispatch_received_date']
        dispatch_dispatch_quantity = request.POST['dispatch_dispatch_quantity']
        dispatch_balance_quantity = request.POST['dispatch_balance_quantity']
        dispatch_rejected_quantity = request.POST['dispatch_rejected_quantity']
        dispatch_bill_number = request.POST['dispatch_bill_number']
        dispatch_bill_file = request.POST['dispatch_bill_file']
        Dispatch.objects.create(dispatch_received_quantity = dispatch_received_quantity,
                                        dispatch_received_date = dispatch_received_date,
                                        dispatch_dispatch_quantity = dispatch_dispatch_quantity,
                                        dispatch_balance_quantity = dispatch_balance_quantity,
                                        dispatch_rejected_quantity = dispatch_rejected_quantity,
                                        dispatch_bill_number = dispatch_bill_number,
                                        dispatch_bill_file = dispatch_bill_file)
        dispatch_object = Dispatch.objects.latest('dispatch_order_date_of_entry') 
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:track_order_details',kwargs={'pk': dispatch_object.pk}))

#Update View
class FabricOrderUpdateView(BSModalUpdateView):
    model = Fabric_Order
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_FabricOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_fabric_order')

class StichingOrderUpdateView(BSModalUpdateView):
    model = Stiching
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_StichingOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_stiching_order')

class WashingOrderUpdateView(BSModalUpdateView):
    model = Washing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_WashingOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_washing_order')

class FinishingOrderUpdateView(BSModalUpdateView):
    model = Finishing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_FinishingOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_finishing_order')

class DispatchOrderUpdateView(BSModalUpdateView):
    model = Dispatch
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_DispatchOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_dispatched_order')
    
class PendingOrderUpdateView(BSModalUpdateView):
    model = Process
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Process_payment_status
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:payment_pending')

class PaidOrderUpdateView(BSModalUpdateView):
    model = Process
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Process_payment_status
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:payment_paid')

""" def user_list(request):
    user_role = request.user.user_role
    users = CustomUser.objects.all()
    #userrole = request.user.user_role
    data = { 'users' : users,'user_role':user_role }
    return render(request,'payment/userlist.html',data) """