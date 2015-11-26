# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20151001_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('cost', models.IntegerField(default=0, blank=True, verbose_name='Cost', null=True)),
                ('start_date', models.DateField(verbose_name='Date of Commencement')),
                ('end_date', models.DateField(blank=True, verbose_name='Date of Completion', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('phone_number', models.CharField(null=True, blank=True, verbose_name='Phone Number', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ContractorPayment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('paid_date', models.DateField(verbose_name='Paid Date')),
                ('remarks', models.CharField(default='', null=True, blank=True, max_length=300)),
                ('contractor', models.ForeignKey(to='projects.Contractor')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2015, 10, 5), verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contractor',
            field=models.ForeignKey(to='projects.Contractor'),
        ),
        migrations.AddField(
            model_name='contract',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
    ]
