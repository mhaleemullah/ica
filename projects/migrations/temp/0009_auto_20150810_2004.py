# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20150810_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='payment_id',
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
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.CharField(max_length=100, verbose_name='Client'),
        ),
    ]
