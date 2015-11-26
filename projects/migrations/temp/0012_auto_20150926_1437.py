# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20150926_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category_id',
            field=models.ForeignKey(blank=True, to='projects.Category', to_field=projects.models.Category, null=True),
        ),
    ]
