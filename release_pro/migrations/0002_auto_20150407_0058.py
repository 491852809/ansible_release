# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release_pro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_group_name', models.CharField(max_length=30)),
                ('pro_group_created_time', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project_item',
            name='pro_group',
            field=models.ForeignKey(related_name=b'project_item', default=0, to='release_pro.Project_Group'),
            preserve_default=False,
        ),
    ]
