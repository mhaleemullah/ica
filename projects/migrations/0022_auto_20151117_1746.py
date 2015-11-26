# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_payment_payment_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeepayment',
            name='type',
            field=models.CharField(max_length=30, choices=[('ADVANCE', 'ADVANCE'), ('SALARY', 'SALARY'), ('TRAVEL', 'TRAVEL'), ('OTHER', 'OTHER'), ('TRANSFERIN', 'TRANSFERIN'), ('TRANSFEROUT', 'TRANSFEROUT')], default='SALARY', verbose_name='Payment As'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Payment'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_details',
            field=models.CharField(choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE'), ('RTGS', 'RTGS')], blank=True, max_length=30, null=True, verbose_name='Paid By'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_from',
            field=models.CharField(max_length=30, choices=[('CLIENT', 'CLIENT'), ('omar & assosciates', 'omar & assosciates')], default='CLIENT'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Project Title'),
        ),
    ]
