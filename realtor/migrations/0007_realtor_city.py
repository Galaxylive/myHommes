# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-17 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20180916_1313'),
        ('realtor', '0006_auto_20180915_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='city',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='property.City'),
        ),
    ]