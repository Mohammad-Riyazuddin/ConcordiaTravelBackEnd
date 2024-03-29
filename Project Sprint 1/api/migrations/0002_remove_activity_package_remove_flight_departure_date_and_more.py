# Generated by Django 5.0.2 on 2024-02-27 04:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='package',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_date',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='package',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='package',
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
