# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_control', '0002_auto_20150519_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
