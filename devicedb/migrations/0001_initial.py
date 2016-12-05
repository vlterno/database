# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pc_id', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200)),
                ('cpu_core', models.CharField(max_length=200)),
                ('cpu_speed', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=200)),
                ('hdd_size', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
    ]
