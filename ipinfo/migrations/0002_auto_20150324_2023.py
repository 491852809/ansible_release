# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip_info',
            name='machine_name',
            field=models.CharField(default='web-yv1', max_length=30, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip_info',
            name='machine_type',
            field=models.CharField(default='ECS', max_length=20, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ip_info',
            name='note',
            field=models.TextField(max_length=50, blank=True),
        ),
    ]
