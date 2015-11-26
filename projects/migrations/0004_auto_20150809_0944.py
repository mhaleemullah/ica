# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150809_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date', default=datetime.date.today)),
                ('shift', models.CharField(max_length=5, default='X', choices=[('A', 'A'), ('I', 'I'), ('X', 'X'), ('XI', 'XI'), ('XX', 'XX')])),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joined_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Joining'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='outstanding',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, null=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee_id',
            field=models.ForeignKey(to='projects.Employee'),
        ),
    ]
