# Generated by Django 2.2.5 on 2019-11-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KNGarment_Order_TrackPro_App', '0013_order_ethenic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fabric_vendor',
            field=models.CharField(blank=True, max_length=920),
        ),
        migrations.AddField(
            model_name='customuser',
            name='finishing_vendor',
            field=models.CharField(blank=True, max_length=920),
        ),
        migrations.AddField(
            model_name='customuser',
            name='stitching_vendor',
            field=models.CharField(blank=True, max_length=920),
        ),
        migrations.AddField(
            model_name='customuser',
            name='washing_vendor',
            field=models.CharField(blank=True, max_length=920),
        ),
    ]