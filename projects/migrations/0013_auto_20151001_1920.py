# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_employeepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2015, 9, 30), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='employeepayment',
            name='remarks',
            field=models.CharField(verbose_name='Remarks', max_length=30, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='paid_details',
            field=models.CharField(choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE')], blank=True, null=True, max_length=30),
        ),
    ]
