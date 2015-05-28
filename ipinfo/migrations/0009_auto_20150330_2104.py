# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipinfo', '0008_auto_20150329_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database_Addr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('database_addr', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Database_Conn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_user', models.CharField(max_length=30)),
                ('data_pass', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Database_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('database_name', models.CharField(max_length=80)),
                ('database_addr', models.ForeignKey(related_name=b'Database_Info', to='ipinfo.Database_Addr')),
                ('database_conn', models.ForeignKey(related_name=b'Database_Info', to='ipinfo.Database_Conn')),
                ('ip_info', models.ForeignKey(related_name=b'Database_Info', to='ipinfo.Ip_Info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ip_info',
            name='master_machine',
            field=models.CharField(default=b'N/A', max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
