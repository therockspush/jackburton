# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 4, 7, 6, 7, 30, 916787, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
