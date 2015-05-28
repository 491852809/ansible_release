# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='group_id',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
