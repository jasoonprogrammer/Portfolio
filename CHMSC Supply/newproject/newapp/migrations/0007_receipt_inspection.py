# Generated by Django 3.1.1 on 2020-10-19 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_auto_20201020_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='inspection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='newapp.inspection'),
            preserve_default=False,
        ),
    ]