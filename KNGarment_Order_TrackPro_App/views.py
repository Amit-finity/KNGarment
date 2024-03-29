#External Imports
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.auth.hashers import make_password
#from django.core.mail import send_mail
from bootstrap_modal_forms.generic import (BSModalCreateView,BSModalUpdateView,BSModalReadView,BSModalDeleteView)

#Project Imports
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch,Order_Mens_Or_Ladies,Order_Kids,Order_Ethenic,CustomUser
from KNGarment_Order_TrackPro_App.forms import Update_Orders,Update_FabricOrder,Update_StichingOrder,Update_WashingOrder,Update_FinishingOrder,Update_DispatchOrder,Update_Process_payment_status,CustomUserForm,Update_FabricOrderProcess,Update_StichingOrderProcess,Update_WashingOrderProcess,Update_FinishingOrderProcess,CustomUserCreationForm,Update_fabric_process_details,Update_stiching_process_details,Update_washing_process_details,Update_finishing_process_details,Update_My_Profile 

from KNGarment_Order_TrackPro_App import functions
# Create your views here.
# ------ Authentication Views -----
# Login
def user_login(request):
    """Logs in a user if the credentials are valid and the user is active,
    else redirects to the same page and displays an error message."""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_new_order_form'))
        else:
            return render(request, 'KNGarment_Order_TrackPro_App/registration/login_form.html',{'error_message': 'Username or Password Incorrect!'})

    else:
        return render(request, 'KNGarment_Order_TrackPro_App/registration/login_form.html')

# Sign Up
def register(request):
    """Registers a user"""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'KNGarment_Order_TrackPro_App/registration/register_form.html',{'error_message':'Passwords do not match!'})
        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'KNGarment_Order_TrackPro_App/registration/register_form.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = CustomUser.objects.create(username=username, password= make_password(password), user_role=2)
            login(request, user)
            return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_new_order_form'))
    else:
        return render(request, 'KNGarment_Order_TrackPro_App/registration/register_form.html')

# Logout
def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:user_login'))

@login_required(login_url='/user_login')
def add_new_order_form(request):
    user_role = request.user.user_role
    data = {'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/Add_orders.html',data)

@login_required(login_url='/user_login')
def update_order_detail(request):
    user_role = request.user.user_role
    orders = Orders.objects.all()
    #logged_in_vendor_order_list = []
    if user_role == 100:
        order_objects = orders
    else:
        values1 = Fabric_Order.objects.filter(process_type=1).all()
        values2 = Stiching.objects.filter(process_type=2).all()
        values3 = Washing.objects.filter(process_type=3).all()
        values4 = Finishing.objects.filter(process_type=4).all()
        for order in orders:
            #vendor_in_one_order = []
            if values1.exists():
                #vendor_in_one_order.append(1)
                logged_in_vendor_order_list = []
                logged_in_vendor_order_list.append(order.pk)
            if values2.exists():
                #vendor_in_one_order.append(2)
                logged_in_vendor_order_list = []
                logged_in_vendor_order_list.append(order.pk)
            if values3.exists():
                #vendor_in_one_order.append(3)
                logged_in_vendor_order_list = []
                logged_in_vendor_order_list.append(order.pk)
            if values4.exists():
                #vendor_in_one_order.append(4)
                logged_in_vendor_order_list = []
                logged_in_vendor_order_list.append(order.pk)
        order_objects = Orders.objects.filter(pk__in=logged_in_vendor_order_list).all()
    #orders = Orders.objects.all()
    data = {'orders':order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/update_orders_detail.html',data)

@login_required(login_url='/user_login')
def add_processes(request,pk):
    user_role = request.user.user_role
    fabric_bill_numbers = Fabric_Order.objects.all()
    order_data = {}
    one_object_of_model_order = Orders.objects.get(pk=pk)
    #order_data['orders']
    order_data['orders'] = one_object_of_model_order
    order_data['fabric_bill_numbers']= fabric_bill_numbers
    order_data['user_role'] = user_role
    if Order_Mens_Or_Ladies.objects.filter(order_mens_or_ladies_order_id=pk).exists():
        order_data['order_mens_or_ladies']=Order_Mens_Or_Ladies.objects.get(order_mens_or_ladies_order_id=pk)
    if Order_Ethenic.objects.filter(order_ethenic_order_id=pk).exists():
        order_data['order_ethenic']=Order_Ethenic.objects.get(order_ethenic_order_id=pk)
    if Order_Kids.objects.filter(order_kids_order_id=pk).exists():
        order_data['order_kids_order']=Order_Kids.objects.get(order_kids_order_id=pk)
    if Fabric_Order.objects.filter(process_order_id=pk).exists():
        order_data['fabric']=Fabric_Order.objects.get(process_order_id=pk)
    if Stiching.objects.filter(process_order_id=pk).exists():
        order_data['stiching']=Stiching.objects.get(process_order_id=pk)
    if Washing.objects.filter(process_order_id=pk).exists():
        order_data['washing']=Washing.objects.get(process_order_id=pk)
    if Finishing.objects.filter(process_order_id=pk).exists():
        order_data['finishing']=Finishing.objects.get(process_order_id=pk)
    #order_kids_object = Order_Kids.objects.filter(order_kids_order_id=pk)
    #order_ethenic_object = Order_Ethenic.objects.filter(order_ethenic_order_id=pk)
    """ fabric_flag
    stitching_flag
    washing_flag
    finishing_flag
    dispatch_flag """
    data = {'order_data':order_data,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/add_processes.html',order_data)

@login_required(login_url='/user_login')
def all_orders(request):
    user_role = request.user.user_role
    all_orders = Orders.objects.all()
    order_status_map_dict = {}
    for order in all_orders:
        length = 0
        status = ""
        process_in_one_order = []
        values1 = Fabric_Order.objects.filter(process_order_id=order.pk)
        values2 = Stiching.objects.filter(process_order_id=order.pk)
        values3 = Washing.objects.filter(process_order_id=order.pk)
        values4 = Finishing.objects.filter(process_order_id=order.pk)
        if values1.exists():
            process_in_one_order.append(1)
        if values2.exists():
            process_in_one_order.append(2)
        if values3.exists():
            process_in_one_order.append(3)
        if values4.exists():
            process_in_one_order.append(4)
        length = len(process_in_one_order)
        #for Current Order
        if length > 0 and length < 4:
            status = "Current"
        #for delivered Order
        if length == 4:
            status = "Dispatch Ready"
        #for Registered Order 
        if length == 0:
            status = "Registered"
        order_status_map_dict[order]=status
    data = {'orders':all_orders,'user_role':user_role,'status':status,'order_status_map_dict':order_status_map_dict}
    return render(request,'KNGarment_Order_TrackPro_App/All_Orders.html',data)

def OrderPaymentSummaryView(request):
    user_role = request.user.user_role
    all_orders = Orders.objects.all()
    order_status_map_dict = {}
    for order in all_orders:
        length = 0
        status = ""
        process_in_one_order = []
        values1 = Fabric_Order.objects.filter(process_order_id=order.pk)
        values2 = Stiching.objects.filter(process_order_id=order.pk)
        values3 = Washing.objects.filter(process_order_id=order.pk)
        values4 = Finishing.objects.filter(process_order_id=order.pk)
        if values1.exists():
            process_in_one_order.append(1)
        if values2.exists():
            process_in_one_order.append(2)
        if values3.exists():
            process_in_one_order.append(3)
        if values4.exists():
            process_in_one_order.append(4)
        length = len(process_in_one_order)
        #for Current Order
        if length > 0 and length < 4:
            status = "Current"
        #for delivered Order
        if length == 4:
            status = "Dispatch Ready"
        #for Registered Order 
        if length == 0:
            status = "Registered"
        order_status_map_dict[order]=status
    data = {'orders':all_orders,'user_role':user_role,'status':status,'order_status_map_dict':order_status_map_dict}
    return render(request,'KNGarment_Order_TrackPro_App/order_payment_summary_list.html',data)

@login_required(login_url='/user_login')
def current_order(request):
    user_role = request.user.user_role
    orders = Orders.objects.all()
    current_order_list = []
   
    for order in orders:
        length = 0
        process_in_one_order = []
        values1 = Fabric_Order.objects.filter(process_order_id=order.pk)
        values2 = Stiching.objects.filter(process_order_id=order.pk)
        values3 = Washing.objects.filter(process_order_id=order.pk)
        values4 = Finishing.objects.filter(process_order_id=order.pk)
        if values1.exists():
            process_in_one_order.append(1)
        if values2.exists():
            process_in_one_order.append(2)
        if values3.exists():
            process_in_one_order.append(3)
        if values4.exists():
            process_in_one_order.append(4)
        length = len(process_in_one_order)
        if length > 0 and length < 4:
            current_order_list.append(order.pk)
    current_order_objects = Orders.objects.filter(pk__in=current_order_list)
    data = {'current_order':current_order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/Current.html',data)

@login_required(login_url='/user_login')
def delivered_order(request):
    user_role = request.user.user_role
    orders = Orders.objects.all()
    delivered_order_list = []
    for order in orders:
        process_in_one_order = []
        length = 0
        values1 = Fabric_Order.objects.filter(process_order_id=order.pk)
        values2 = Stiching.objects.filter(process_order_id=order.pk)
        values3 = Washing.objects.filter(process_order_id=order.pk)
        values4 = Finishing.objects.filter(process_order_id=order.pk)
        if values1.exists():
            process_in_one_order.append(1)
        if values2.exists():
            process_in_one_order.append(2)
        if values3.exists():
            process_in_one_order.append(3)
        if values4.exists():
            process_in_one_order.append(4)
        length = len(process_in_one_order)
        if length == 4:
            delivered_order_list.append(order.pk)
    delivered_order_objects = Orders.objects.filter(pk__in=delivered_order_list)
    data = {'delivered_order':delivered_order_objects,'length':length,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/delivered_orders.html',data)

@login_required(login_url='/user_login')
def track_order_registered_order(request):
    user_role = request.user.user_role
    orders = Orders.objects.all()
    registered_order_list = []
    
    for order in orders:
        length = 0
        process_in_one_order = []
        values1 = Fabric_Order.objects.filter(process_order_id=order.pk)
        values2 = Stiching.objects.filter(process_order_id=order.pk)
        values3 = Washing.objects.filter(process_order_id=order.pk)
        values4 = Finishing.objects.filter(process_order_id=order.pk)
        if values1.exists():
            process_in_one_order.append(1)
        if values2.exists():
            process_in_one_order.append(2)
        if values3.exists():
            process_in_one_order.append(3)
        if values4.exists():
            process_in_one_order.append(4)
        length = len(process_in_one_order)
        if length == 0:
            registered_order_list.append(order.pk)
    registered_order_objects = Orders.objects.filter(pk__in=registered_order_list)
    data = {'registered_order':registered_order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/Order_registered.html',data)

""" @login_required(login_url='/user_login')
def track_order_details(request,pk):
    user_role = request.user.user_role
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
            'dispatch':dispatch_object,
            'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/Order_Details_2.html',data) """

@login_required(login_url='/user_login')
def track_order_fabric_order(request):
    user_role = request.user.user_role
    if user_role == 100:
        fabric_order_objects = Fabric_Order.objects.all()
    else:
        pk = request.user.pk
        fabric_order_objects = Fabric_Order.objects.filter(process_customuser_id=pk).all()
    data = {'fabric_order':fabric_order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/fabric_order.html',data)


@login_required(login_url='/user_login')
def track_order_stiching_order(request):
    user_role = request.user.user_role
    if user_role == 100:
        stiching_order_objects = Stiching.objects.all()
    else:
        pk = request.user.pk
        stiching_order_objects = Stiching.objects.filter(process_customuser_id=pk).all()
    data = {'stiching_order':stiching_order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/stiching.html',data)

@login_required(login_url='/user_login')
def track_order_washing_order(request):
    user_role = request.user.user_role
    if user_role == 100:
        washing_order_objects = Washing.objects.all()
    else:
        pk = request.user.pk
        washing_order_objects = Washing.objects.filter(process_customuser_id=pk).all()
    data = {'washing_order':washing_order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/Washing.html',data)

@login_required(login_url='/user_login')
def track_order_finishing_order(request):
    user_role = request.user.user_role
    if user_role == 100:
        finishing_order_objects = Finishing.objects.all()
    else:
        pk = request.user.pk
        finishing_order_objects = Finishing.objects.filter(process_customuser_id=pk).all()
    data = {'finishing_order':finishing_order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/Finishing.html',data)

@login_required(login_url='/user_login')
def track_order_dispatched_order(request):
    user_role = request.user.user_role
    dispatch_order_objects = Dispatch.objects.all()
    data = {'dispatch_order':dispatch_order_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/dispatch.html',data)

@login_required(login_url='/user_login')
def payment_pending(request):
    user_role = request.user.user_role
    process_objects = Process.objects.all().filter(process_payment_status=2)
    data = {'processes':process_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/pending_order.html',data)

@login_required(login_url='/user_login')
def payment_paid(request):
    user_role = request.user.user_role
    process_objects = Process.objects.all().filter(process_payment_status=1)
    data = {'processes':process_objects,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/paid_order.html',data)

@login_required(login_url='/user_login')
def reports_job_worker_balancereport(request):
    user_role = request.user.user_role
    data = {'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/job_worker_bal_report.html',data)

@login_required(login_url='/user_login')
def reports_stockreport(request):
    user_role = request.user.user_role
    data = {'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/stock_report.html',data)

@login_required(login_url='/user_login')
def track_order_production_details(request):
    user_role = request.user.user_role
    data = {'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/Production.html',data)

@login_required(login_url='/user_login')
def report_error(request):
    user_role = request.user.user_role
    data = {'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/report_error.html',data)

@login_required(login_url='/user_login')
def forget_password(request):
    user_role = request.user.user_role
    data = {'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/forget_password.html',data)

@login_required(login_url='/user_login')
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

        if request.POST.get('mens_or_ladies_checkbox', False) == 'mens_or_ladies_checkbox':
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
        
        if request.POST.get('kids_checkbox', False) == 'kids_checkbox': 
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

        if request.POST.get('ethenic_checkbox', False) == 'ethenic_checkbox':
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

@login_required(login_url='/user_login')
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
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_processes',kwargs={'pk': Order_object.pk}))

@login_required(login_url='/user_login')
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
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_processes',kwargs={'pk': Order_object.pk}))

@login_required(login_url='/user_login')
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
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_processes',kwargs={'pk': Order_object.pk}))

@login_required(login_url='/user_login')
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
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_processes',kwargs={'pk': Order_object.pk}))

@login_required(login_url='/user_login')
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
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_processes',kwargs={'pk': dispatch_object.pk}))

#fabric_order_vendor_payment view
def fabric_order_vendor_payment(request):
    fabric_list=functions.filtering_vendors(1)
    user_role = request.user.user_role
    data = {'fabric_list':fabric_list,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/fabric_order_vendor_payment.html',data)

#fabric_order_vendor_payment_details view
def fabric_order_vendor_payment_details(request,vendor_id,payment_status):
    user_role = request.user.user_role
    fabric_objects = Fabric_Order.objects.filter(process_customuser_id=vendor_id,process_payment_status=payment_status).all()
    data = {"user_role":user_role, "fabric_objects": fabric_objects }
    return render(request,'KNGarment_Order_TrackPro_App/fabric_order_vendor_payment_details.html',data)

#stiching_order_vendor_payment view
def stiching_order_vendor_payment(request):
    stiching_list=functions.filtering_vendors(2)
    user_role = request.user.user_role
    data = {'stiching_list':stiching_list,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/stiching_order_vendor_payment.html',data)

#stiching_order_vendor_payment_details view
def stiching_order_vendor_payment_details(request,vendor_id,payment_status):
    user_role = request.user.user_role
    stiching_objects = Stiching.objects.filter(process_customuser_id=vendor_id,process_payment_status=payment_status).all()
    data = {"user_role":user_role, "stiching_objects": stiching_objects }
    return render(request,'KNGarment_Order_TrackPro_App/stiching_order_vendor_payment_details.html',data)

#washing_order_vendor_payment view
def washing_order_vendor_payment(request):
    washing_list=functions.filtering_vendors(3)
    user_role = request.user.user_role
    data = {'washing_list':washing_list,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/washing_order_vendor_payment.html',data)

#washing_order_vendor_payment_details view
def washing_order_vendor_payment_details(request,vendor_id,payment_status):
    user_role = request.user.user_role
    washing_objects = Washing.objects.filter(process_customuser_id=vendor_id,process_payment_status=payment_status).all()
    data = {"user_role":user_role, "washing_objects": washing_objects }
    return render(request,'KNGarment_Order_TrackPro_App/washing_order_vendor_payment_details.html',data)

#finishing_order_vendor_payment view
def finishing_order_vendor_payment(request):
    finishing_list=functions.filtering_vendors(4)
    user_role = request.user.user_role
    data = {'finishing_list':finishing_list,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/finishing_order_vendor_payment.html',data)

#finishing_order_vendor_payment_details view
def finishing_order_vendor_payment_details(request,vendor_id,payment_status):
    user_role = request.user.user_role
    finishing_objects = Finishing.objects.filter(process_customuser_id=vendor_id,process_payment_status=payment_status).all()
    data = {"user_role":user_role, "finishing_objects": finishing_objects }
    return render(request,'KNGarment_Order_TrackPro_App/finishing_order_vendor_payment_details.html',data)

#Summary View
def order_summary(request,pk):
    order_data = {}
    one_object_of_model_order = Orders.objects.get(pk=pk)
    order_data['orders'] = one_object_of_model_order
    if Order_Mens_Or_Ladies.objects.filter(order_mens_or_ladies_order_id=pk).exists():
        order_data['order_mens_or_ladies']=Order_Mens_Or_Ladies.objects.get(order_mens_or_ladies_order_id=pk)
    if Order_Ethenic.objects.filter(order_ethenic_order_id=pk).exists():
        order_data['order_ethenic']=Order_Ethenic.objects.get(order_ethenic_order_id=pk)
    if Order_Kids.objects.filter(order_kids_order_id=pk).exists():
        order_data['order_kids_order']=Order_Kids.objects.get(order_kids_order_id=pk)
    if Fabric_Order.objects.filter(process_order_id=pk).exists():
        order_data['fabric']=Fabric_Order.objects.get(process_order_id=pk)
    if Stiching.objects.filter(process_order_id=pk).exists():
        order_data['stiching']=Stiching.objects.get(process_order_id=pk)
    if Washing.objects.filter(process_order_id=pk).exists():
        order_data['washing']=Washing.objects.get(process_order_id=pk)
    if Finishing.objects.filter(process_order_id=pk).exists():
        order_data['finishing']=Finishing.objects.get(process_order_id=pk)
    return render(request,'KNGarment_Order_TrackPro_App/summary.html',order_data)

def my_profile(request,pk):
    users = CustomUser.objects.get(pk=pk)
    user_data = {}
    user_data['users'] = users
    user_data['user_role'] = users.user_role
    return render(request,'KNGarment_Order_TrackPro_App/my_profile.html',user_data)

class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'KNGarment_Order_TrackPro_App/sign_up.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:userlist')


#Update View
class AllOrdersUpdateView(BSModalUpdateView):
    model = Orders 
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Orders
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:all_orders')

#Delete View
class AllOrdersDeleteView(BSModalDeleteView):
    model = Orders
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:all_orders')

#Update View
class RegisteredOrdersUpdateView(BSModalUpdateView):
    model = Orders 
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Orders
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_registered_order')

#Delete View
class RegisteredOrdersDeleteView(BSModalDeleteView):
    model = Orders
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_registered_order')

#Update View
class CurrentOrdersUpdateView(BSModalUpdateView):
    model = Orders 
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Orders
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:current_order')

#Delete View
class CurrentOrdersDeleteView(BSModalDeleteView):
    model = Orders
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:current_order')

class DeliveredOrdersUpdateView(BSModalUpdateView):
    model = Orders 
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Orders
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:delivered_order')

#Delete View
class DeliveredOrdersDeleteView(BSModalDeleteView):
    model = Orders
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:delivered_order')




@method_decorator(login_required, name='dispatch')
class FabricOrderUpdateView(BSModalUpdateView):
    model = Fabric_Order
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_FabricOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_fabric_order')

@method_decorator(login_required, name='dispatch')
class StichingOrderUpdateView(BSModalUpdateView):
    model = Stiching
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_StichingOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_stiching_order')

@method_decorator(login_required, name='dispatch')
class WashingOrderUpdateView(BSModalUpdateView):
    model = Washing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_WashingOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_washing_order')

@method_decorator(login_required, name='dispatch')
class FinishingOrderUpdateView(BSModalUpdateView):
    model = Finishing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_FinishingOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_finishing_order')

@method_decorator(login_required, name='dispatch')
class DispatchOrderUpdateView(BSModalUpdateView):
    model = Dispatch
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_DispatchOrder
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:track_order_dispatched_order')
    
@method_decorator(login_required, name='dispatch')
class PendingOrderUpdateView(BSModalUpdateView):
    model = Process
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Process_payment_status
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:payment_pending')

@method_decorator(login_required, name='dispatch')
class PaidOrderUpdateView(BSModalUpdateView):
    model = Process
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_Process_payment_status
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:payment_paid')

@login_required(login_url='/user_login')
def user_list(request):
    user_role = request.user.user_role
    users = CustomUser.objects.all()
    #userrole = request.user.user_role
    data = { 'users' : users,'user_role':user_role}
    return render(request,'KNGarment_Order_TrackPro_App/userlist.html',data)

#< -----Update Users Views ------>
@method_decorator(login_required, name='dispatch')
class UserUpdateView(BSModalUpdateView):
    model = CustomUser
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = CustomUserForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:userlist')
#</-----Update Users Views ------>

#< -----Delete Users Views ------>
@method_decorator(login_required, name='dispatch')
class UserDeleteView(BSModalDeleteView):
    model = CustomUser
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:userlist')
#</-----Delete Users Views ------>

#< -----Add Users Views ------>
@method_decorator(login_required, name='dispatch')
class Add_UsersView(BSModalCreateView):
    template_name = 'KNGarment_Order_TrackPro_App/add_new_user.html'
    form_class = CustomUserForm
    success_message = 'Success: User was added.'
    success_url = reverse_lazy('KNGarment_Order_TrackPro_App:userlist')

class FabricOrderProcessUpdateView(BSModalUpdateView):
    model = Fabric_Order
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_FabricOrderProcess
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        fabric_object = Fabric_Order.objects.get(pk=self.kwargs['pk'])
        pk = fabric_object.process_order_id
        return reverse_lazy('KNGarment_Order_TrackPro_App:add_processes', kwargs={'pk': pk })

class StichingOrderProcessUpdateView(BSModalUpdateView):
    model = Stiching
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_StichingOrderProcess
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        stiching_object = Stiching.objects.get(pk=self.kwargs['pk'])
        pk = stiching_object.process_order_id
        return reverse_lazy('KNGarment_Order_TrackPro_App:add_processes', kwargs={'pk': pk })        

class WashingOrderProcessUpdateView(BSModalUpdateView):
    model = Washing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_WashingOrderProcess
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        washing_object = Washing.objects.get(pk=self.kwargs['pk'])
        pk = washing_object.process_order_id
        return reverse_lazy('KNGarment_Order_TrackPro_App:add_processes', kwargs={'pk': pk })  
          
class FinishingOrderProcessUpdateView(BSModalUpdateView):
    model = Finishing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_FinishingOrderProcess
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        finishing_object = Finishing.objects.get(pk=self.kwargs['pk'])
        pk = finishing_object.process_order_id
        return reverse_lazy('KNGarment_Order_TrackPro_App:add_processes', kwargs={'pk': pk })  

class FabricProcessUpdateView(BSModalUpdateView):
    model = Fabric_Order
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_fabric_process_details
    success_message = 'Success: Entry was updated.'

    def get_success_url(self,**kwargs):
        Fabric_Order_Model_Object = Fabric_Order.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Fabric_Order_Model_Object.process_customuser_id.pk
        payment_status = Fabric_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:fabric_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })

class FabricOrderProcessDeleteView(BSModalDeleteView):
    model = Fabric_Order
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        Fabric_Order_Model_Object = Fabric_Order.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Fabric_Order_Model_Object.process_customuser_id.pk
        payment_status = Fabric_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:fabric_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })



class StichingProcessUpdateView(BSModalUpdateView):
    model = Stiching
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_stiching_process_details
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Stiching_Order_Model_Object = Stiching.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Stiching_Order_Model_Object.process_customuser_id.pk
        payment_status = Stiching_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:stiching_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })

class StichingProcessDeleteView(BSModalDeleteView):
    model = Stiching
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        Stiching_Order_Model_Object = Stiching.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Stiching_Order_Model_Object.process_customuser_id.pk
        payment_status = Stiching_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:stiching_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })

class WashingProcessUpdateView(BSModalUpdateView):
    model = Washing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_washing_process_details
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Washing_Order_Model_Object = Washing.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Washing_Order_Model_Object.process_customuser_id.pk
        payment_status = Washing_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:washing_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })

class WashingProcessDeleteView(BSModalDeleteView):
    model = Washing
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    
    def get_success_url(self,**kwargs):
        Washing_Order_Model_Object = Washing.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Washing_Order_Model_Object.process_customuser_id.pk
        payment_status = Washing_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:washing_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })

class FinishingProcessUpdateView(BSModalUpdateView):
    model = Finishing
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_finishing_process_details
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Finishing_Order_Model_Object = Finishing.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Finishing_Order_Model_Object.process_customuser_id.pk
        payment_status = Finishing_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:finishing_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })

class FinishingProcessDeleteView(BSModalDeleteView):
    model = Finishing
    template_name = 'KNGarment_Order_TrackPro_App/delete_entry.html'
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Finishing_Order_Model_Object = Finishing.objects.get(pk=self.kwargs['pk'])
        process_customuser_id = Finishing_Order_Model_Object.process_customuser_id.pk
        payment_status = Finishing_Order_Model_Object.process_payment_status
        return reverse_lazy('KNGarment_Order_TrackPro_App:finishing_order_vendor_payment_details', kwargs={'vendor_id':process_customuser_id,'payment_status':payment_status })

class MyProfileUpdateView(BSModalUpdateView):
    model = CustomUser
    template_name = 'KNGarment_Order_TrackPro_App/update_order.html'
    form_class = Update_My_Profile
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Customuser_Model_Object = CustomUser.objects.get(pk=self.kwargs['pk'])
        customuser_pk = Customuser_Model_Object.pk
        return reverse_lazy('KNGarment_Order_TrackPro_App:my_profile', kwargs={'pk':customuser_pk})

#</-----Add Users Views ------>    