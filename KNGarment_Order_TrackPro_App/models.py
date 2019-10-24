#<---------Django Imported Libraries--------->
from django.db import models
from django.utils import timezone
from datetime import datetime
#</---------Django Imported Libraries--------->

#<---------External Libraries--------->
from model_utils.managers import InheritanceManager
#</---------External Libraries--------->

# Create your models here.

#Client Model
class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=920)

    def __str__(self):
        return str(self.pk)

#Vendor Model
class Vendor(models.Model):
    vendor_id = models.IntegerField()
    vendor_name = models.CharField(max_length=920)
    vendor_type = models.CharField(max_length=920)
    vendor_balance_stock = models.FloatField()
    
    def __str__(self):
        return str(self.pk)

# Orders Model
class Orders(models.Model):
    order_order_number = models.CharField(max_length=920)
    order_order_type = models.CharField(max_length=920)
    order_order_brands = models.CharField(max_length=920)
    order_order_style_number = models.CharField(max_length=920)
    order_order_fit = models.CharField(max_length=920)
    order_order_quantity = models.IntegerField()
    order_order_date = models.DateField(default=timezone.now)
    order_delivery_date = models.DateField(default=timezone.now)
    order_order_category = models.CharField(max_length=920)
    order_fit_sample_status = models.CharField(max_length=920)
    order_fit_sample_submitted_date = models.DateField(default=timezone.now)
    order_pps_sample_status = models.CharField(max_length=920)
    order_pps_sample_submitted_date = models.DateField(default=timezone.now)
    order_order_remark = models.CharField(max_length=920,blank=True)
    order_order_date_of_entry = models.DateTimeField(default=timezone.now)
    order_client_id = models.ForeignKey(Client, on_delete = models.CASCADE,default=1)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Orders List"
        verbose_name = "Order"

#Process(Model Relationship Building [Parent Model])  
class Process(models.Model):
    process_vendor_name = models.CharField(max_length=920,blank=True)
    process_vendor_location = models.CharField(max_length=920,blank=True)
    process_received_quantity = models.IntegerField(blank=True,null=True)
    process_received_date = models.DateField(default=timezone.now)
    process_delivery_date = models.DateField(default=timezone.now)
    process_bill_number = models.IntegerField(blank=True,default=0)
    process_bill_file = models.FileField(blank=True)
    process_payment_status = models.CharField(max_length=920,blank=True)
    process_date_of_entry = models.DateTimeField(default=timezone.now)
    process_vendor_id = models.ForeignKey(Vendor, on_delete = models.CASCADE,blank=True)
    process_order_id = models.ForeignKey(Orders, on_delete=models.CASCADE,blank=True)
    objects = InheritanceManager()

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Process List"
        verbose_name = "Process"

#Fabric Order[Child Model]
class Fabric_Order(Process):
    fabric_order_sort_number = models.CharField(max_length=920)
    fabric_order_quantity = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Fabric Orders List"
        verbose_name = "Fabric Order"

#Stiching[Child Model]
class Stiching(Process):
    stiching_average_one = models.FloatField()
    stiching_average_two = models.FloatField()
    stiching_average_three = models.FloatField()
    stiching_rate_one = models.FloatField()
    stiching_rate_two = models.FloatField()
    stiching_rate_three = models.FloatField()
    stiching_opening_fabric_stock = models.IntegerField()
    stiching_opening_stock_date = models.DateField(default=timezone.now)
    stiching_fabric_bill_date = models.DateField(default=timezone.now)
    stiching_fabric_used = models.CharField(max_length=920)
    stiching_fabric_bill_number = models.CharField(max_length=920,blank=True)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Stiching Orders List"
        verbose_name = "Stiching Order"

#Washing[Child Model]
class Washing(Process):
    washing_process_name = models.CharField(max_length=920)
    washing_rate = models.IntegerField()
    washing_order_date = models.DateField(default=timezone.now)
    washing_delivery_quantity = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Washing Orders List"
        verbose_name = "Washing Order"

#Finishing [Child Model]
class Finishing(Process):
    finishing_rate = models.IntegerField()
    finishing_delivery_quantity = models.IntegerField()
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Finishing Orders List"
        verbose_name = "Finishing Order"

#Dispatch model
class Dispatch(models.Model):
    dispatch_received_quantity = models.IntegerField()
    dispatch_received_date = models.DateField(default=timezone.now)
    dispatch_dispatch_quantity = models.IntegerField()
    dispatch_balance_quantity = models.IntegerField()
    dispatch_rejected_quantity = models.IntegerField()
    dispatch_bill_number = models.IntegerField()
    dispatch_bill_file = models.FileField()
    dispatch_payment_status = models.CharField(max_length=920)
    dispatch_order_date_of_entry = models.DateField(default=timezone.now)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Dispatch Orders List"
        verbose_name = "Dispatch Order"