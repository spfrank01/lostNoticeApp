# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lostNoitceApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savelostnoitce',
            old_name='detail_item_lost',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='savelostnoitce',
            old_name='email_owner_item_lost',
            new_name='name_item',
        ),
        migrations.RenameField(
            model_name='savelostnoitce',
            old_name='time_submit_item_lost',
            new_name='time_submit',
        ),
        migrations.RenameField(
            model_name='savelostnoitce',
            old_name='name_item_lost',
            new_name='your_email',
        ),
        migrations.RenameField(
            model_name='savelostnoitce',
            old_name='owner_item_lost',
            new_name='your_name',
        ),
        migrations.RenameField(
            model_name='savelostnoitce',
            old_name='telephone_number_owner_item_lost',
            new_name='your_telephone',
        ),
    ]
