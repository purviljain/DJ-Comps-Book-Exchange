# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-09 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_in', '0005_auto_20180306_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default='images/default_user.png', upload_to='profile pics/'),
        ),
    ]
