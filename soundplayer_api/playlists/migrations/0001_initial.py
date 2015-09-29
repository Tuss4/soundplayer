# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scloud_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('scloud_url', models.URLField()),
                ('listener', models.ForeignKey(related_name='playlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
