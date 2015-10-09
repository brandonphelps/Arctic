# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thunderdome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='loser',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
