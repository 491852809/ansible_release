# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0006_log_save_ip_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_save',
            name='ip_info',
            field=models.ForeignKey(related_name=b'log_save', to='ipinfo.Ip_Info'),
        ),
    ]
