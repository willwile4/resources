# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='am_i_stupid',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
