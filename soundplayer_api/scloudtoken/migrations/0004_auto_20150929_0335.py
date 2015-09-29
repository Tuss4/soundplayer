# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('scloudtoken', '0003_auto_20150928_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundcloudtoken',
            name='listener',
            field=models.OneToOneField(related_name='scloud_token', to=settings.AUTH_USER_MODEL),
        ),
    ]
