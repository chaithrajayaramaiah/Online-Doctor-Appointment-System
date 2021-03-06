# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docdetails',
            name='descp',
        ),
        migrations.RemoveField(
            model_name='docdetails',
            name='pswd',
        ),
        migrations.RemoveField(
            model_name='docdetails',
            name='spclztn',
        ),
        migrations.RemoveField(
            model_name='docdetails',
            name='uname',
        ),
        migrations.AddField(
            model_name='docdetails',
            name='Address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='City',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='Landmark',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='PIN',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='State',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='experience',
            field=models.PositiveIntegerField(blank=0, default=0),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='fees',
            field=models.PositiveIntegerField(blank=0, default=0),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='slot1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='slot2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='slot3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='slot4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='slot5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='slot6',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='slot7',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdetails',
            name='specialization',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='docdetails',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='docdetails',
            name='first_name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='docdetails',
            name='last_name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='docdetails',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
