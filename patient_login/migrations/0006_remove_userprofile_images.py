# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_login', '0005_userprofile_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='images',
        ),
    ]
