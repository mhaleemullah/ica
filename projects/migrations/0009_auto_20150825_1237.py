# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_expense_remarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.AddField(
            model_name='attendance',
            name='project',
            field=models.ForeignKey(blank=True, null=True, to='projects.Project'),
        ),
    ]
