# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150809_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='shift',
            field=models.IntegerField(choices=[(0, 'A'), (1, 'I'), (2, 'X'), (3, 'XI'), (4, 'XX')], default=2),
        ),
    ]
