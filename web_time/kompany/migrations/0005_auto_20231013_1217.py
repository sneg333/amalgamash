# Generated by Django 3.2.12 on 2023-10-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]