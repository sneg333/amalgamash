# Generated by Django 3.2.23 on 2023-12-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0007_auto_20231219_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pop_prodaj',
            field=models.BooleanField(default=False, verbose_name='популярные товары'),
        ),
    ]
