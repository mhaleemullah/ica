# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_remove_expense_payment_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_from',
            field=models.CharField(default='CLIENT', max_length=30, choices=[('CLIENT', 'CLIENT'), ('SELF', 'SELF')]),
            preserve_default=False,
        ),
    ]
