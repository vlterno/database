# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devicedb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nb_id', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200)),
                ('cpu_core', models.CharField(max_length=200)),
                ('cpu_speed', models.CharField(max_length=200)),
                ('hdd_type', models.CharField(max_length=200)),
                ('hdd_size', models.CharField(max_length=200)),
                ('screen_size', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200)),
                ('product_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sp_id', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200)),
                ('cpu_core', models.CharField(max_length=200)),
                ('cpu_speed', models.CharField(max_length=200)),
                ('flash_size', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('lte', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
    ]
