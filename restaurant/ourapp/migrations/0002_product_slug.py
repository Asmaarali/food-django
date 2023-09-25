# Generated by Django 4.2.5 on 2023-09-20 20:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_name', unique=True),
        ),
    ]
