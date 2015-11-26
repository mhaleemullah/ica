# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150809_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particulars', models.CharField(max_length=200, blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('amount', models.IntegerField(default=0)),
                ('paid_details', models.CharField(choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE')], max_length=30, blank=True, null=True)),
                ('paid_date', models.DateField(blank=True, null=True, verbose_name='Paid Date')),
                ('dealer_id', models.ForeignKey(to='projects.Dealer')),
                ('project_id', models.ForeignKey(blank=True, to='projects.Project', null=True)),
            ],
        ),
    ]
