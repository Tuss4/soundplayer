# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listeners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listener',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listener',
            name='soundcloud_username',
            field=models.CharField(default=0, unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='listener',
            unique_together=set([('email', 'soundcloud_username')]),
        ),
    ]
