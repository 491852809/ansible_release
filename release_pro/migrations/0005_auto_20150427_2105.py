# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0004_project_item_pro_ansi_release_yml'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log_save',
            name='log_add',
        ),
        migrations.AddField(
            model_name='log_save',
            name='log_complex',
            field=models.CharField(default=datetime.date(2015, 4, 27), max_length=3000, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='log_save',
            name='log_type',
            field=models.CharField(default=1, max_length=300, blank=True),
            preserve_default=False,
        ),
    ]
