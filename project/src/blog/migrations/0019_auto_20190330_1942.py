# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-03-30 23:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190330_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 30, 23, 42, 20, 144920, tzinfo=utc)),
        ),
    ]
