# Generated by Django 4.1.7 on 2023-03-09 02:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_alter_filter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
