# Generated by Django 3.1.1 on 2020-10-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0010_auto_20201028_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='newenduser',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
