# Generated by Django 5.0.2 on 2024-02-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_flight_arrival_time_flight_departure_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='departure_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]