from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch,Order_Mens_Or_Ladies,Order_Kids,Order_Ethenic,CustomUser

def filtering_vendors(vendor_type_parameter):
    vendor_payment_status = [1,2]
    x = list(set(list(CustomUser.objects.filter(user_role=vendor_type_parameter).values_list('pk','username'))))
    vendor_status_list = [vendor_payment_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
    vendor_dict = dict(zip(x,final))
    return vendor_dict

def vendor_payment_count(a,vendor_payment_status_one):
    if vendor_payment_status_one == 1:
        count = Process.objects.filter(process_customuser_id=CustomUser.objects.get(pk=int(a[0])),process_payment_status=1).all().count()
        return count
    elif vendor_payment_status_one == 2:
        count = Process.objects.filter(process_customuser_id=CustomUser.objects.get(pk=int(a[0])),process_payment_status=2).all().count()
        return count