# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0006_auto_20150408_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['created_at']},
        ),
    ]
