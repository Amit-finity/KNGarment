# Generated by Django 2.2.5 on 2019-10-31 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KNGarment_Order_TrackPro_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('client_name', models.CharField(max_length=920)),
            ],
        ),
    ]
