# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0005_auto_20150408_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_at',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
