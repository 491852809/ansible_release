# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0009_auto_20150511_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_item',
            name='pro_ansi_backup_yml',
            field=models.CharField(default=1, max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
