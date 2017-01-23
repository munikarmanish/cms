# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 09:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinate_list', to=settings.AUTH_USER_MODEL, verbose_name='Supervisor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
    ]
