# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_auto_20141216_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='parent',
            field=models.ForeignKey(blank=True, to='loginapp.members', null=True),
            preserve_default=True,
        ),
    ]
