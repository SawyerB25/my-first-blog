# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_model_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='model_pic',
        ),
    ]
