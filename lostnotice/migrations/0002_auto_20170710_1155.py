# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-10 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostnotice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostnoticelist',
            name='time_submit',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]