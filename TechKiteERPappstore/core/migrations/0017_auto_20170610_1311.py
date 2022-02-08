# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170325_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='ocsid',
        ),
        migrations.AlterField(
            model_name='app',
            name='admin_docs',
            field=models.URLField(blank=True, max_length=256, verbose_name='Admin documentation URL'),
        ),
        migrations.AlterField(
            model_name='app',
            name='developer_docs',
            field=models.URLField(blank=True, max_length=256, verbose_name='Developer documentation URL'),
        ),
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.CharField(help_text='app ID, identical to folder name', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='app',
            name='issue_tracker',
            field=models.URLField(blank=True, max_length=256, verbose_name='Issue tracker URL'),
        ),
        migrations.AlterField(
            model_name='app',
            name='user_docs',
            field=models.URLField(blank=True, max_length=256, verbose_name='User documentation URL'),
        ),
        migrations.AlterField(
            model_name='apprelease',
            name='download',
            field=models.URLField(blank=True, max_length=256, verbose_name='Archive download URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(help_text='Category ID used to identify the category an app is uploaded to', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='TechKiteERPrelease',
            name='is_current',
            field=models.BooleanField(default=False, help_text='Only one version can be the current one. This field is used to pre-select dropdowns for app generation, etc.', verbose_name='Is current version'),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='url',
            field=models.URLField(max_length=256, verbose_name='Image URL'),
        ),
    ]