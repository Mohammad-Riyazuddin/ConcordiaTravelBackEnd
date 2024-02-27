# Generated by Django 5.0.2 on 2024-02-27 05:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_city_rename_arrival_date_flight_arrival_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination_city',
            field=models.CharField(max_length=100),
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='arrival_datetime',
            new_name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_datetime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='status',
        ),
        migrations.AddField(
            model_name='flight',
            name='airport',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.activity'),
        ),
        migrations.AddField(
            model_name='package',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.flight'),
        ),
        migrations.AddField(
            model_name='package',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.hotel'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airlines',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
