# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20151001_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentExpense',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='dealer_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='particulars',
        ),
        migrations.AddField(
            model_name='payment',
            name='remarks',
            field=models.CharField(blank=True, null=True, verbose_name='Remarks', default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='employeepayment',
            name='remarks',
            field=models.CharField(blank=True, null=True, verbose_name='Remarks', max_length=300),
        ),
        migrations.AlterField(
            model_name='expense',
            name='paid_details',
            field=models.CharField(blank=True, null=True, choices=[('CASH', 'CASH'), ('CREDIT', 'CREDIT')], max_length=30),
        ),
        migrations.AlterField(
            model_name='expense',
            name='remarks',
            field=models.CharField(blank=True, null=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_details',
            field=models.CharField(blank=True, null=True, choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE'), ('RTGS', 'RTGS')], max_length=30),
        ),
        migrations.AddField(
            model_name='paymentexpense',
            name='bill',
            field=models.ForeignKey(to='projects.Expense'),
        ),
        migrations.AddField(
            model_name='paymentexpense',
            name='payment',
            field=models.ForeignKey(to='projects.Payment'),
        ),
    ]
