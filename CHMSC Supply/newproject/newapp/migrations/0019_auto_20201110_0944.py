# Generated by Django 3.1.1 on 2020-11-10 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0018_inventorymonitoring_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='series',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventorymonitoring',
            name='balance',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventorymonitoring',
            name='onhand',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventorymonitoring',
            name='series',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventorymonitoring',
            name='shortage',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='no',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='qty',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='newenduser',
            name='count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='series',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='term_of_delivery',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
