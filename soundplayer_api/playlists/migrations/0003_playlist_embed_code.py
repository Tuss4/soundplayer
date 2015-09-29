# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_auto_20150929_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='embed_code',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
