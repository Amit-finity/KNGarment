# Generated by Django 2.2.5 on 2019-10-31 05:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KNGarment_Order_TrackPro_App', '0003_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_order_number', models.CharField(max_length=920)),
                ('order_order_type', models.CharField(max_length=920)),
                ('order_order_brands', models.CharField(max_length=920)),
                ('order_order_style_number', models.CharField(max_length=920)),
                ('order_order_fit', models.CharField(max_length=920)),
                ('order_order_quantity', models.IntegerField()),
                ('order_order_date', models.DateField(default=django.utils.timezone.now)),
                ('order_delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('order_order_category', models.CharField(max_length=920)),
                ('order_fit_sample_status', models.CharField(max_length=920)),
                ('order_fit_sample_submitted_date', models.DateField(default=django.utils.timezone.now)),
                ('order_pps_sample_status', models.CharField(max_length=920)),
                ('order_pps_sample_submitted_date', models.DateField(default=django.utils.timezone.now)),
                ('order_order_remark', models.CharField(blank=True, max_length=920)),
                ('order_order_date_of_entry', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_client_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='KNGarment_Order_TrackPro_App.Client')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders List',
            },
        ),
    ]
