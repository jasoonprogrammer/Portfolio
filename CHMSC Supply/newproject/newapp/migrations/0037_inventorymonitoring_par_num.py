# Generated by Django 3.1.1 on 2021-03-11 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0036_auto_20210302_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorymonitoring',
            name='par_num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.parnumber'),
        ),
    ]