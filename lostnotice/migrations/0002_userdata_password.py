# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostnotice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='password',
            field=models.CharField(default=123456, max_length=100),
            preserve_default=False,
        ),
    ]
