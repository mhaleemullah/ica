# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20151006_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='payment_from',
            field=models.CharField(choices=[('CLIENT', 'CLIENT'), ('SELF', 'SELF')], blank=True, null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2015, 11, 16), verbose_name='Date'),
        ),
    ]
