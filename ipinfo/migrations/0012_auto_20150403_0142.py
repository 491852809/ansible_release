# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0011_auto_20150331_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_save',
            name='log_add',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
