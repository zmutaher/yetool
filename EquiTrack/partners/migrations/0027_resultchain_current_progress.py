# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0026_auto_20160229_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultchain',
            name='current_progress',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
