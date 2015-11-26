# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20151117_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='payment_from',
        ),
    ]
