# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='routewx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dep', models.CharField(max_length=4)),
                ('arr', models.CharField(max_length=4)),
                ('alt', models.CharField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
