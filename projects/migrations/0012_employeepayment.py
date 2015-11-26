# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20150926_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('paid_date', models.DateField(verbose_name='Paid Date')),
                ('month', models.IntegerField(choices=[(1, 'January'), (2, 'Febrauary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1, verbose_name='For the Month')),
                ('year', models.IntegerField(default=2015, verbose_name='For the Year')),
                ('type', models.CharField(choices=[('ADVANCE', 'ADVANCE'), ('SALARY', 'SALARY'), ('TRAVEL', 'TRAVEL'), ('OTHER', 'OTHER')], verbose_name='Payment As', max_length=30, default='SALARY')),
                ('remarks', models.CharField(max_length=30, verbose_name='Remarks')),
                ('employee', models.ForeignKey(to='projects.Employee')),
            ],
        ),
    ]
