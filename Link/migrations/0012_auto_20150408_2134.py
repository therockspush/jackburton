# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0011_auto_20150408_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_at',
            field=models.DateTimeField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='image',
            field=models.ImageField(max_length=200, upload_to=b'static/preferredroutes/images/stories/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(max_length=555, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
