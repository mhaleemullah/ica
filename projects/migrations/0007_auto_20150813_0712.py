# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='shift',
            field=models.IntegerField(default=2, choices=[(0, 'A'), (1, '/'), (2, 'X'), (3, 'XI'), (4, 'XX'), (5, 'XXI'), (6, 'XXX'), (6, 'XXXI'), (6, 'XXXX')]),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(blank=True, verbose_name='Date', null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='invoice_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='paid_details',
            field=models.CharField(choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE'), ('RTGS', 'RTGS')], blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(verbose_name='Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.CharField(verbose_name='Client', max_length=100),
        ),
    ]
