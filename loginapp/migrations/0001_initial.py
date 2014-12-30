# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=60, null=True, verbose_name=b'UserName')),
                ('gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('user_id', models.CharField(unique=True, max_length=50, verbose_name=b'User_ID')),
                ('password', models.CharField(max_length=30, verbose_name=b'Password')),
                ('email_id', models.EmailField(max_length=254, verbose_name=b'Email_ID')),
                ('resident_location', models.CharField(max_length=50, verbose_name=b'Resident Location')),
                ('contact_no', models.CharField(max_length=30, verbose_name=b'Contact No.', blank=True)),
                ('status', models.CharField(max_length=10, null=True, verbose_name=b'Status', choices=[(b'A', b'Active'), (b'I', b'Inactive')])),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rolename', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=40, choices=[(b'A', b'Active'), (b'I', b'Inactive')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='members',
            name='role',
            field=models.ForeignKey(to='loginapp.role'),
            preserve_default=True,
        ),
    ]
