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
            name='SoundcloudToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
                ('expiry', models.DateTimeField()),
                ('listener', models.ForeignKey(related_name='scloud_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
