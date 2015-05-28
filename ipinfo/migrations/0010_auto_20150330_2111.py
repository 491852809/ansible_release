# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0009_auto_20150330_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='database_addr',
            name='id',
        ),
        migrations.AlterField(
            model_name='database_addr',
            name='database_addr',
            field=models.CharField(max_length=80, serialize=False, primary_key=True),
        ),
    ]
