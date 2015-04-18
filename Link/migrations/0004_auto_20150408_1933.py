# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0003_auto_20150407_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='link',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 4, 8, 19, 33, 3, 28870, tzinfo=utc), auto_now=True, auto_now_add=True),
            preserve_default=False,
        ),
    ]
