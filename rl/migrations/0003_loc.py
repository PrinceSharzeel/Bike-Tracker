# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-23 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rl', '0002_auto_20160622_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('lon', models.CharField(max_length=75)),
                ('lat', models.CharField(max_length=75)),
                ('date', models.CharField(max_length=75)),
                ('link', models.CharField(max_length=75)),
            ],
        ),
    ]