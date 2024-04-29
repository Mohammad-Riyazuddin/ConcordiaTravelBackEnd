# Generated by Django 5.0.2 on 2024-04-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_booking_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('CUSTOMER', 'Customer'), ('AGENT', 'Agent'), ('ADMIN', 'ADMIN')], max_length=10),
        ),
    ]
