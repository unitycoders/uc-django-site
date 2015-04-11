# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def createModel(apps, schema_editor):
    Category = apps.get_model("lectern", "Category")
    category = Category()
    category.title = "Miscellaneous"
    category.slug = "misc"
    category.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lectern', '0003_category'),
    ]

    operations = [
        migrations.RunPython(createModel),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, to='lectern.Category'),
            preserve_default=False,
        ),
    ]
