# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostNoitceApp', '0002_auto_20170419_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('time_register', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
