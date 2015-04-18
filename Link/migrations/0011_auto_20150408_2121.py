# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0010_auto_20150408_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
