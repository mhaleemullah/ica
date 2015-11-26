# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20151006_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='remarks',
            field=models.CharField(default='', blank=True, null=True, max_length=300),
        ),
        migrations.AddField(
            model_name='contractor',
            name='remarks',
            field=models.CharField(default='', blank=True, null=True, max_length=300),
        ),
        migrations.AddField(
            model_name='contractor',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=30, verbose_name='Status'),
        ),
    ]
