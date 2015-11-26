# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category_id',
            field=models.ForeignKey(blank=True, to='projects.Category', null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='dealer_id',
            field=models.ForeignKey(blank=True, to='projects.Dealer', null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='project_id',
            field=models.ForeignKey(blank=True, to='projects.Project', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name=b'Date of Commencement'),
        ),
    ]
