# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-23 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elle', '0003_auto_20190523_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='image_url',
            new_name='image',
        ),
    ]
