# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0002_auto_20150407_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_reset',
            name='process_script',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project_item',
            name='pro_ansi_codedir',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project_item',
            name='pro_ansi_yml',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project_item',
            name='pro_name',
            field=models.CharField(max_length=100),
        ),
    ]
