# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('name', models.CharField(max_length=5)),
                ('position', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('school', models.CharField(max_length=100)),
                ('points', models.DecimalField(decimal_places=1, max_digits=3)),
                ('rebounds', models.DecimalField(decimal_places=1, max_digits=3)),
                ('assists', models.DecimalField(decimal_places=1, max_digits=3)),
                ('steals', models.DecimalField(decimal_places=1, max_digits=3)),
                ('blocks', models.DecimalField(decimal_places=1, max_digits=3)),
                ('shooting_percentage', models.DecimalField(decimal_places=3, max_digits=4)),
                ('three_point_percentage', models.DecimalField(decimal_places=3, max_digits=4)),
                ('free_throw_percentage', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
    ]
