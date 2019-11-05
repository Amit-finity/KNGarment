from django.contrib import admin
from django.urls import path,re_path
from django.urls import reverse_lazy
from KNGarment_Order_TrackPro_App import views

app_name = 'KNGarment_Order_TrackPro_App'

urlpatterns = [
# --- Pages Urls ---
# ------ Authentication URLs -----
#Login
path("" , views.user_login, name="user_login"),

#register URL
path('register/', views.register, name = 'register'),

#forget_password URL
path('forget_password/', views.forget_password, name = 'forget_password'),

#report_error URL
path('report_error/', views.report_error, name = 'report_error'),
#path('report_error_submit/', views.report_error_submit, name ='report_error_submit'),
#path('report_error_success/', views.report_error_success, name ='report_error_success'),



# Logout
path('logout/', views.user_sign_out, name='logout'),
# </------ Authentication URLs -----

# ------ Sidemenu Urls ------
#add_new_order Form URL
path("add_new_order_form/", views.add_new_order_form, name = 'add_new_order_form'),

#update_order_detail URL
path("update_order_detail/",views.update_order_detail,name='update_order_detail'),


#add_processes URL
path('add_processes/<int:pk>', views.add_processes, name = 'add_processes'),

#all_orders URL
path('all_orders/', views.all_orders, name = 'all_orders'),

#current_order URL
path('current_order/', views.current_order, name = 'current_order'),

#delivered_order URL
path('delivered_order/', views.delivered_order, name = 'delivered_order'),

#track_order_registered_order URL
path('track_order_registered_order/', views.track_order_registered_order, name = 'track_order_registered_order'),

#track_order_details URL
#path('track_order_details/<int:pk>', views.track_order_details, name = 'track_order_details'),

#track_order_fabric_order URL
path('track_order_fabric_order/', views.track_order_fabric_order, name = 'track_order_fabric_order'),

#track_order_stiching_order URL
path('track_order_stiching_order/', views.track_order_stiching_order, name = 'track_order_stiching_order'),

#track_order_washing_order URL
path('track_order_washing_order/', views.track_order_washing_order, name = 'track_order_washing_order'),

#track_order_finishing_order URL
path('track_order_finishing_order/', views.track_order_finishing_order, name = 'track_order_finishing_order'),

#track_order_dispatched_order URL
path('track_order_dispatched_order/', views.track_order_dispatched_order, name = 'track_order_dispatched_order'),

#payment_pending URL
path('payment_pending/', views.payment_pending, name = 'payment_pending'),

#payment_paid URL
path('payment_paid/', views.payment_paid, name = 'payment_paid'),

#pending_order_v2 URL
path('pending_order_v2/',views.pending_order_v2,name='pending_order_v2'),

#paid_order_v2 URL
path('paid_order_v2/',views.paid_order_v2,name='paid_order_v2'),

#reports_job_worker_balancereport URL
path('reports_job_worker_balancereport/', views.reports_job_worker_balancereport, name = 'reports_job_worker_balancereport'),

#reports_stockreport URL
path('reports_stockreport/', views.reports_stockreport, name = 'reports_stockreport'),
# </------ Sidemenu Urls ------

#track_order_production_details URL
path('track_order_production_details/', views.track_order_production_details, name = 'track_order_production_details'),

#<------ All Form Submit Processing URL -----------
#------add_new_order_form_submit URL -----
path('add_new_order_form_submit/', views.add_new_order_form_submit, name='add_new_order_form_submit'),

path('add_new_fabric_order_form_submit/', views.add_new_fabric_order_form_submit, name='add_new_fabric_order_form_submit'),

path('add_new_stiching_form_submit/', views.add_new_stiching_form_submit, name='add_new_stiching_form_submit'),

path('add_new_washing_order_form_submit/', views.add_new_washing_order_form_submit, name='add_new_washing_order_form_submit'),

path('add_new_finishing_order_form_submit/', views.add_new_finishing_order_form_submit, name='add_new_finishing_order_form_submit'),

path('add_new_dispatch_order_form_submit/', views.add_new_dispatch_order_form_submit, name='add_new_dispatch_order_form_submit'),

#AddProcesses Page
#Fabric Order Process Update
path('fabric_order_process_update/<int:pk>',views.FabricOrderProcessUpdateView.as_view(), name='fabric_order_process_update'),

#Stiching Order Process Update
path('stiching_order_process_update/<int:pk>',views.StichingOrderProcessUpdateView.as_view(), name='stiching_order_process_update'),

#Washing Order Process Update
path('washing_order_process_update/<int:pk>',views.WashingOrderProcessUpdateView.as_view(), name='washing_order_process_update'),

#Finishing Order Process Update
path('finishing_order_process_update/<int:pk>',views.FinishingOrderProcessUpdateView.as_view(), name='finishing_order_process_update'),

#All Orders - Update
path('all_order_update/<int:pk>',views.AllOrdersUpdateView.as_view(), name='all_order_update'),

#All Orders - Delete
path('all_order_delete/<int:pk>',views.AllOrdersDeleteView.as_view(),name='all_order_delete'),

#Registered Orders - Update
path('registered_order_update/<int:pk>',views.RegisteredOrdersUpdateView.as_view(), name='registered_order_update'),

#Registered Orders - Delete
path('registered_order_delete/<int:pk>',views.RegisteredOrdersDeleteView.as_view(),name='registered_order_delete'),

#Current Orders - Update
path('current_order_update/<int:pk>',views.CurrentOrdersUpdateView.as_view(), name='current_order_update'),

#Current Orders - Delete
path('current_order_delete/<int:pk>',views.CurrentOrdersDeleteView.as_view(),name='current_order_delete'),

#Delivered Orders - Update
path('delivered_order_update/<int:pk>',views.DeliveredOrdersUpdateView.as_view(), name='delivered_order_update'),

#Delivered Orders - Delete
path('delivered_order_delete/<int:pk>',views.DeliveredOrdersDeleteView.as_view(),name='delivered_order_delete'),

# Fabric Order - Update
path('fabric_order_update/<int:pk>',views.FabricOrderUpdateView.as_view(), name='fabric_order_update'),

# Stiching Order - Update
path('stiching_order_update/<int:pk>',views.StichingOrderUpdateView.as_view(), name='stiching_order_update'),

# Washing Order - Update
path('washing_order_update/<int:pk>',views.WashingOrderUpdateView.as_view(), name='washing_order_update'),

# Finishing Order - Update
path('finishing_order_update/<int:pk>',views.FinishingOrderUpdateView.as_view(), name='finishing_order_update'),

# Dispatch Order - Update
path('dispatch_order_update/<int:pk>',views.DispatchOrderUpdateView.as_view(), name='dispatch_order_update'),

# Pending Order - Update
path('pending_order_update/<int:pk>',views.PendingOrderUpdateView.as_view(), name='pending_order_update'),

# Paid Order - Update
path('paid_order_update/<int:pk>',views.PaidOrderUpdateView.as_view(), name='paid_order_update'),


# ------- Portal Users URls ---------
#< -----Users list Urls ------>
path('users/', views.user_list, name='userlist'),
#</-----Users list Urls------>


#< -----Add Users Urls ------>
path('add_users/',views.Add_UsersView.as_view(),name='add_users'),
#</-----Add Users Urls ------>

#< -----Delete Users Urls ------>
path('userdelete/<int:pk>',views.UserDeleteView.as_view(),name='userdelete'),
#</-----Delete Users Urls ------>

#< -----Update Users Urls ------>
path('userupdate/<int:pk>',views.UserUpdateView.as_view(),name='userupdate'),
#</-----Update Users Urls ------>
# </------- Portal Users URls ---------

]

