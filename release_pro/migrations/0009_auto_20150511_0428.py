# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0008_auto_20150428_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_group',
            name='pro_ansi_process_directory_reset_yml',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
