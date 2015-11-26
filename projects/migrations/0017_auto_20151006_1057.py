# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20151006_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('paid_date', models.DateField(verbose_name='Paid Date')),
                ('remarks', models.CharField(default='', null=True, blank=True, max_length=300)),
                ('contractor', models.ForeignKey(to='projects.Contractor')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='contractorpayment',
            name='contractor',
        ),
        migrations.RemoveField(
            model_name='contractorpayment',
            name='project',
        ),
        migrations.DeleteModel(
            name='ContractorPayment',
        ),
    ]
