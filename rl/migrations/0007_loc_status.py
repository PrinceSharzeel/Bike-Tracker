# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-24 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rl', '0006_adder'),
    ]

    operations = [
        migrations.AddField(
            model_name='loc',
            name='status',
            field=models.CharField(default='false', max_length=75),
        ),
    ]
