# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0007_project_item_pro_ansi_process_directory_reset_yml'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_item',
            name='pro_ansi_process_directory_reset_yml',
        ),
        migrations.AddField(
            model_name='project_group',
            name='pro_ansi_process_directory_reset_yml',
            field=models.CharField(default='/data/ansible/Rstprocess/', max_length=100),
            preserve_default=False,
        ),
    ]
