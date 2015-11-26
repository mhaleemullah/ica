# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('owner', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, verbose_name=b'Acquired Date', blank=True)),
                ('invoice_no', models.IntegerField(null=True, blank=True)),
                ('particulars', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('paid_details', models.CharField(blank=True, max_length=30, null=True, choices=[(b'CASH', b'CASH'), (b'CHEQUE', b'CHEQUE')])),
                ('paid_date', models.DateField(null=True, verbose_name=b'Paid Date', blank=True)),
                ('category_id', models.ForeignKey(to='projects.Category')),
                ('dealer_id', models.ForeignKey(to='projects.Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('owner', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Date of Commencement')),
                ('end_date', models.DateField(null=True, verbose_name=b'Date of Completion', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='project_id',
            field=models.ForeignKey(to='projects.Project'),
        ),
    ]
