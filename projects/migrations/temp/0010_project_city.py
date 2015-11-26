# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150810_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
