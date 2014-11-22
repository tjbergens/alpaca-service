# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accountName', models.CharField(default=b'', max_length=100, blank=True)),
                ('userName', models.CharField(default=b'', max_length=100, blank=True)),
                ('password', models.CharField(default=b'', max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
