# Generated by Django 5.0.2 on 2024-03-26 22:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_description',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_status',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='num_people',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='cancel_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]