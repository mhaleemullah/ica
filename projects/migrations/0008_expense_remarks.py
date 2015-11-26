# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150813_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='remarks',
            field=models.CharField(default='', max_length=300),
        ),
    ]
