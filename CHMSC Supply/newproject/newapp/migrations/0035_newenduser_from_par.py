# Generated by Django 3.1.1 on 2021-03-01 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0034_newenduser_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='newenduser',
            name='from_par',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.pars'),
        ),
    ]