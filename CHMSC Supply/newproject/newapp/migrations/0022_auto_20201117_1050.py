# Generated by Django 3.1.1 on 2020-11-17 02:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0021_auto_20201117_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorymonitoring',
            name='date_transferred',
        ),
        migrations.AddField(
            model_name='newenduser',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]