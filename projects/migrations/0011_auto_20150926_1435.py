# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20150825_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(verbose_name='Date', default=datetime.date(2015, 9, 25)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, null=True, verbose_name='Designation', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='outstanding',
            field=models.IntegerField(blank=True, null=True, default=0, verbose_name='Outstanding'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, null=True, verbose_name='Phone Number', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(blank=True, null=True, default=0, verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], verbose_name='Status', default='ACTIVE', max_length=30),
        ),
    ]
