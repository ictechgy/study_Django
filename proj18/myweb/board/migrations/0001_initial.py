# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField(default=0)),
                ('good_count', models.IntegerField(default=0)),
                ('bad_count', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('board_id', models.IntegerField()),
                ('author', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=250)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
