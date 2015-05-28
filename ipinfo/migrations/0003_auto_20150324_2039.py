# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0002_auto_20150324_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_info',
            name='expire_time',
            field=models.CharField(default=b'N/A', max_length=30, blank=True),
        ),
    ]
