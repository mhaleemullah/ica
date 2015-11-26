# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150810_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='project',
        ),
        migrations.AddField(
            model_name='employee',
            name='payment_id',
            field=models.ForeignKey(to='projects.Payment', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category_id',
            field=models.ForeignKey(to='projects.Category'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='dealer_id',
            field=models.ForeignKey(to='projects.Dealer'),
        ),
    ]
