# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectern', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('url', models.URLField()),
                ('article', models.ForeignKey(to='lectern.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
