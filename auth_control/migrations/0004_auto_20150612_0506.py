# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_control', '0003_auto_20150525_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='above_img',
            field=models.ImageField(default='', upload_to=b'up_img', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='bottom_img',
            field=models.ImageField(default=1, upload_to=b'down_img', blank=True),
            preserve_default=False,
        ),
    ]
