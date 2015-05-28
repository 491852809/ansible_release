# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0010_auto_20150330_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_save',
            name='username',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
