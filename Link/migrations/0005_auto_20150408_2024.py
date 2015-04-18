# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0004_auto_20150408_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'get_latest_by': 'created_at'},
        ),
    ]
