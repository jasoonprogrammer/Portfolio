# Generated by Django 3.1.1 on 2021-02-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0030_auto_20210214_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorymonitoring',
            name='purpose',
        ),
        migrations.AddField(
            model_name='inspection',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
    ]
