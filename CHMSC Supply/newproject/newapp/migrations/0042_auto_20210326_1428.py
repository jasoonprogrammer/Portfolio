# Generated by Django 3.1.1 on 2021-03-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0041_remove_inventorymonitoring_transferred_to_new_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorymonitoring',
            name='equipment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='NewEndUser',
        ),
    ]
