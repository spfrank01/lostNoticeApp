# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-10 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostnotice', '0003_auto_20170710_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='time_register',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
