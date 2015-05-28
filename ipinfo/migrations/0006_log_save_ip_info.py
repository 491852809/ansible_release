# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0005_auto_20150324_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_save',
            name='ip_info',
            field=models.ForeignKey(related_name=b'Log_Save', default=1, to='ipinfo.Ip_Info'),
            preserve_default=False,
        ),
    ]
