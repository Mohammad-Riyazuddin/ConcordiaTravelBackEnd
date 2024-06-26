# Generated by Django 5.0.2 on 2024-03-31 19:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_booking_bookingcost_alter_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingCost',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
