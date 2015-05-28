# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('innerip', models.IPAddressField(blank=True)),
                ('outerip', models.IPAddressField(blank=True)),
                ('Eth0Mac', models.CharField(max_length=30, blank=True)),
                ('Eth1Mac', models.CharField(max_length=30, blank=True)),
                ('cpu', models.CharField(max_length=10, blank=True)),
                ('memory', models.CharField(max_length=20, blank=True)),
                ('disk_large', models.CharField(max_length=20, blank=True)),
                ('bandwidth', models.CharField(max_length=20, blank=True)),
                ('expire_time', models.CharField(default=b'N/A', max_length=30)),
                ('register_time', models.DateField(default=django.utils.timezone.now)),
                ('note', models.TextField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log_Save',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('log_add', models.CharField(max_length=100, blank=True)),
                ('log_time', models.DateField(default=django.utils.timezone.now)),
                ('username', models.ForeignKey(related_name=b'log_save', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Login_Mode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=30, blank=True)),
                ('password', models.CharField(max_length=30, blank=True)),
                ('ip_info', models.ForeignKey(related_name=b'login_mode', to='ipinfo.Ip_Info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firm', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('master', models.CharField(max_length=30, blank=True)),
                ('pro_name', models.CharField(max_length=30, blank=True)),
                ('domain', models.CharField(max_length=50, blank=True)),
                ('pro_dir', models.CharField(max_length=40, blank=True)),
                ('ip_info', models.ForeignKey(related_name=b'project_info', to='ipinfo.Ip_Info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ip_info',
            name='place',
            field=models.ForeignKey(related_name=b'ip_info', to='ipinfo.Place'),
            preserve_default=True,
        ),
    ]
