# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0007_auto_20150324_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_info',
            name='register_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='log_save',
            name='log_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
