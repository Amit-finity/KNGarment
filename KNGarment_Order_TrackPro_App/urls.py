from django.contrib import admin
from django.urls import path,re_path
from django.urls import reverse_lazy
from KNGarment_Order_TrackPro_App import views

app_name = 'KNGarment_Order_TrackPro_App'

urlpatterns = [
# --- Pages Urls ---
# ------ Authentication URLs -----
#Login
path("user_login/" , views.user_login, name="user_login"),

#forget_password URL
path('forget_password/', views.forget_password, name = 'forget_password'),

# Logout
#path('logout/', views.user_sign_out, name='logout'),

#report_error URL
path('report_error/', views.report_error, name = 'report_error'),
#path('report_error_submit/', views.report_error_submit, name ='report_error_submit'),
#path('report_error_success/', views.report_error_success, name ='report_error_success'),

#register URL
path('register/', views.register, name = 'register'),

# Logout
path('logout/', views.user_sign_out, name='logout'),
# </------ Authentication URLs -----

# ------ Sidemenu Urls ------
#add_new_order Form URL
path("", views.add_new_order_form, name = 'add_new_order_form'),

#add_processes URL
path('add_processes/<int:pk>', views.add_processes, name = 'add_processes'),

#current_order URL
path('current_order/', views.current_order, name = 'current_order'),

#delivered_order URL
path('delivered_order/', views.delivered_order, name = 'delivered_order'),

#track_order_registered_order URL
path('track_order_registered_order/', views.track_order_registered_order, name = 'track_order_registered_order'),

#track_order_details URL
path('track_order_details/<int:pk>', views.track_order_details, name = 'track_order_details'),

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

]

