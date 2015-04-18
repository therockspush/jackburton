# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0002_link_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='image',
            field=models.ImageField(upload_to=b'static/preferredroutes/images/stories/'),
            preserve_default=True,
        ),
    ]
