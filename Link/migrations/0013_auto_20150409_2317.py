# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0012_auto_20150408_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='image',
            field=s3direct.fields.S3DirectField(),
            preserve_default=True,
        ),
    ]
