# Generated by Django 3.1.1 on 2020-09-28 11:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FundSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('series', models.IntegerField()),
                ('date_received', models.DateField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.campus')),
            ],
        ),
        migrations.CreateModel(
            name='InspectionOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ItemUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModeOfProcurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NewEndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiveStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RequestingEndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RequisitioningOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('contact', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.level')),
            ],
            options={
                'verbose_name': 'System User',
                'verbose_name_plural': 'System Users',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.receipttype')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('series', models.IntegerField()),
                ('date_received_by_supplier', models.DateField()),
                ('date_received_by_bac', models.DateField()),
                ('term_of_delivery', models.IntegerField()),
                ('amounts', models.FloatField()),
                ('remarks', models.TextField()),
                ('date_recorded', models.DateField(default=django.utils.timezone.now)),
                ('fund_source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.fundsource')),
                ('mode_of_procurement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.modeofprocurement')),
                ('requesting_end_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.requestingenduser')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('desc', models.CharField(max_length=254)),
                ('qty', models.IntegerField()),
                ('cost', models.FloatField()),
                ('acc_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.accountcode')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.article')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.inspection')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.unit')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('onhand', models.IntegerField()),
                ('shortage', models.IntegerField(blank=True, default=None, null=True)),
                ('overage', models.IntegerField()),
                ('series', models.IntegerField()),
                ('date_transfered', models.DateField(blank=True, default=None, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.item')),
                ('remarks', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.itemuser')),
                ('transferred_to_new_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='newapp.newenduser')),
            ],
        ),
        migrations.AddField(
            model_name='inspection',
            name='inspection_officer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.inspectionofficer'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='po',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.purchaseorder'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='receive_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.receivestatus'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='requisitioning_office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newapp.requisitioningoffice'),
        ),
    ]
