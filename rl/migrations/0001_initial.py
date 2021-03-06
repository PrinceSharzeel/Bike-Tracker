# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumni_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_id', models.CharField(blank=True, max_length=30)),
                ('linkedin_profile_api_url', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('join_date', models.DateTimeField()),
                ('joined_with_linkedin', models.BooleanField(default=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='alumni_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('location', models.CharField(default='<Not Available>', max_length=50)),
                ('picture_url', models.CharField(blank=True, max_length=75)),
                ('company', models.CharField(default='<Not Available>', max_length=50)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('linkedin_public_profile', models.CharField(blank=True, max_length=100)),
                ('branch', models.CharField(max_length=75)),
                ('contact', models.CharField(default='<Not Available>', max_length=25)),
                ('yog', models.IntegerField()),
                ('username', models.CharField(max_length=50, unique=True)),
                ('about', models.TextField(default='A Proud Malviyan', max_length=250)),
                ('public_contact', models.BooleanField(default=False)),
                ('public_email', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='feedbackmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=75)),
                ('feedback', models.TextField(max_length=300)),
            ],
        ),
    ]
