# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='choices',
            name='q_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='choices',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
