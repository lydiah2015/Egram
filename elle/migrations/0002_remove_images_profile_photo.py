# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='profile_photo',
        ),
    ]
