# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_employeepayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category_id',
            field=models.ForeignKey(null=True, to='projects.Category', blank=True),
        ),
    ]
