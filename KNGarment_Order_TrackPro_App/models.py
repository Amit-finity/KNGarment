#<---------Django Imported Libraries--------->
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime
#</---------Django Imported Libraries--------->

#<---------External Libraries--------->
from model_utils.managers import InheritanceManager
#</---------External Libraries--------->

#<---------Custom User Model --------->
class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 108
    ADMIN = 100
    FABRIC_VENDOR = 1
    STITCHING_VENDOR = 2
    WASHING_VENDOR = 3
    FINISHING_VENDOR = 4
    ROLE_CHOICES = (
      (ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin'),
      (FABRIC_VENDOR,'fabric_vendor'),
      (STITCHING_VENDOR,'stitching_vendor'),
      (WASHING_VENDOR,'washing_vendor'),
      (FINISHING_VENDOR,'finishing_vendor')
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN,blank=True)
    
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
    Paid = 1
    Pending = 2
    PAYMENT_STATUS=((Paid,'Paid'), (Pending,'Pending'))
    process_vendor_name = models.CharField(max_length=920,blank=True)
    process_vendor_location = models.CharField(max_length=920,blank=True)
    process_received_quantity = models.IntegerField(blank=True,null=True)
    process_received_date = models.DateField(default=timezone.now)
    process_delivery_date = models.DateField(default=timezone.now)
    process_bill_number = models.IntegerField(blank=True,default=0)
    process_bill_file = models.FileField(blank=True)
    process_payment_status = models.PositiveSmallIntegerField(choices=PAYMENT_STATUS,default=Pending,blank=True)
    process_date_of_entry = models.DateTimeField(default=timezone.now)
    process_vendor_id = models.ForeignKey(Vendor, on_delete = models.CASCADE,blank=True)
    process_order_id = models.ForeignKey(Orders, on_delete=models.CASCADE,blank=True)
    process_customuser_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=1)
    objects = InheritanceManager()

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Process List"
        verbose_name = "Process"

#Fabric Order[Child Model]
class Fabric_Order(Process):
    Fabric_Order = 1
    process_type = models.PositiveSmallIntegerField(default=Fabric_Order)
    fabric_order_sort_number = models.CharField(max_length=920)
    fabric_order_quantity = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Fabric Orders List"
        verbose_name = "Fabric Order"

#Stiching[Child Model]
class Stiching(Process):
    Stiching = 2
    process_type = models.PositiveSmallIntegerField(default=Stiching)
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
    Washing = 3
    process_type = models.PositiveSmallIntegerField(default=Washing)
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
    Finishing = 4
    process_type = models.PositiveSmallIntegerField(default=Finishing)
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
    dispatch_order_date_of_entry = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Dispatch Orders List"
        verbose_name = "Dispatch Order"

class Order_Mens_Or_Ladies(models.Model):
    order_mens_or_ladies_size_26_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_28_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_30_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_32_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_34_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_36_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_38_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_40_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_42_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_size_44_quantity = models.CharField(max_length=920,blank=True)
    order_mens_or_ladies_order_id = models.ForeignKey(Orders, on_delete = models.CASCADE,blank=True)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Mens Or Ladies Orders List"
        verbose_name = "Mens Or Ladies Order"

class Order_Kids(models.Model):
    order_kids_age_2_years = models.CharField(max_length=920,blank=True)
    order_kids_age_3to4_years = models.CharField(max_length=920,blank=True)
    order_kids_age_5to6_years = models.CharField(max_length=920,blank=True)
    order_kids_age_7to8_years = models.CharField(max_length=920,blank=True)
    order_kids_age_9to10_years = models.CharField(max_length=920,blank=True)
    order_kids_age_11to12_years = models.CharField(max_length=920,blank=True)
    order_kids_age_13to14_years = models.CharField(max_length=920,blank=True)
    order_kids_age_15to16_years = models.CharField(max_length=920,blank=True)
    order_kids_age_2to3_years = models.CharField(max_length=920,blank=True)
    order_kids_age_4to5_years = models.CharField(max_length=920,blank=True)
    order_kids_age_6to7_years = models.CharField(max_length=920,blank=True)
    order_kids_age_8to9_years = models.CharField(max_length=920,blank=True)
    order_kids_age_10to11_years = models.CharField(max_length=920,blank=True)
    order_kids_order_id = models.ForeignKey(Orders, on_delete = models.CASCADE,blank=True)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Kids Orders List"
        verbose_name = "Kids Order"

class Order_Ethenic(models.Model):
    order_ethenic_size_XS = models.CharField(max_length=920,blank=True)
    order_ethenic_size_S = models.CharField(max_length=920,blank=True)
    order_ethenic_size_M = models.CharField(max_length=920,blank=True)
    order_ethenic_size_L = models.CharField(max_length=920,blank=True)
    order_ethenic_size_XL = models.CharField(max_length=920,blank=True)
    order_ethenic_size_XXL = models.CharField(max_length=920,blank=True)
    order_ethenic_size_XXXL = models.CharField(max_length=920,blank=True)
    order_ethenic_order_id = models.ForeignKey(Orders, on_delete = models.CASCADE,blank=True)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Ethenic Orders List"
        verbose_name = "Ethenic Order"












