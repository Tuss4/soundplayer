# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scloudtoken', '0002_auto_20150928_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundcloudtoken',
            name='refresh_token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
