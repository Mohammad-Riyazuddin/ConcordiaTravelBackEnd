# Generated by Django 5.0.2 on 2024-03-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_booking_booking_date_alter_booking_cancel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Canceled', 'Canceled')], default='Booked', max_length=10),
        ),
    ]
