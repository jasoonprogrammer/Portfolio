# Generated by Django 3.1.1 on 2020-09-28 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20200929_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newenduser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='newenduser',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='newenduser',
            name='middle_i',
            field=models.CharField(max_length=1),
        ),
    ]
