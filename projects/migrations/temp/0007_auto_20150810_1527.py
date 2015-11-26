# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='shift',
            field=models.IntegerField(default=2, choices=[(0, 'A'), (1, '/'), (2, 'X'), (3, 'XI'), (4, 'XX'), (5, 'XXI'), (6, 'XXX'), (6, 'XXXI'), (6, 'XXXX')]),
        ),
        migrations.AlterField(
            model_name='expense',
            name='paid_details',
            field=models.CharField(blank=True, max_length=30, choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE'), ('RTGS', 'RTGS')], null=True),
        ),
    ]
