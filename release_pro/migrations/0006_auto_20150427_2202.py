# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0005_auto_20150427_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log_save',
            name='pro_item',
        ),
        migrations.AddField(
            model_name='log_save',
            name='pro_group',
            field=models.ForeignKey(related_name=b'log_save', default=1, to='release_pro.Project_Group'),
            preserve_default=False,
        ),
    ]
