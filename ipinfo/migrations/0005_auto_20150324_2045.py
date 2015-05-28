# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0004_auto_20150324_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_info',
            name='domain',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
