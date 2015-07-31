# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0003_auto_20150407_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_item',
            name='pro_ansi_release_yml',
            field=models.CharField(default='/data/ansible/gan/release.yml', max_length=100),
            preserve_default=False,
        ),
    ]
