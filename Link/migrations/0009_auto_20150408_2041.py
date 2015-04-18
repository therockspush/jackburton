# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0008_auto_20150408_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='blurb',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
