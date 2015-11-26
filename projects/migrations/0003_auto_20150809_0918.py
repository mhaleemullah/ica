# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150801_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.IntegerField(default=0)),
                ('joined_date', models.DateField(verbose_name='Date of Joining')),
                ('status', models.CharField(max_length=30, default='ACTIVE', choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')])),
                ('outstanding', models.IntegerField(default=0)),
                ('phone_number', models.CharField(max_length=15)),
                ('category_id', models.ForeignKey(null=True, to='projects.Category', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(verbose_name='Acquired Date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='paid_date',
            field=models.DateField(verbose_name='Paid Date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='paid_details',
            field=models.CharField(max_length=30, choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(verbose_name='Date of Completion', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='Date of Commencement'),
        ),
    ]
