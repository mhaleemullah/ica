# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20151117_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='payment_from',
            field=models.CharField(choices=[('CLIENT', 'CLIENT'), ('SELF', 'SELF')], default='CLIENT', max_length=10),
            preserve_default=False,
        ),
    ]
