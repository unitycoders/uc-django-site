# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectern', '0004_article_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField(blank=True)),
                ('category', models.ForeignKey(to='lectern.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
