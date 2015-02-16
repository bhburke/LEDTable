# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('option_type', models.CharField(max_length=6, choices=[(b'INT', b'Integer'), (b'COLOR', b'Color'), (b'COLORS', b'ColorList')])),
                ('animation', models.ForeignKey(to='interface.Animation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
