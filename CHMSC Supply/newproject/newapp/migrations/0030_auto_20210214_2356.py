# Generated by Django 3.1.1 on 2021-02-14 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0029_remove_pars_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.classification'),
        ),
    ]
