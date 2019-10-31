# Generated by Django 2.2.5 on 2019-10-31 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KNGarment_Order_TrackPro_App', '0010_dispatch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Mens_Or_Ladies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_mens_or_ladies_size_26_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_28_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_30_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_32_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_34_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_36_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_38_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_40_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_42_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_size_44_quantity', models.CharField(blank=True, max_length=920)),
                ('order_mens_or_ladies_order_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='KNGarment_Order_TrackPro_App.Orders')),
            ],
            options={
                'verbose_name': 'Mens Or Ladies Order',
                'verbose_name_plural': 'Mens Or Ladies Orders List',
            },
        ),
    ]