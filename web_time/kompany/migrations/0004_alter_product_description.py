# Generated by Django 3.2.12 on 2023-10-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0003_auto_20231009_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='срок поставки'),
        ),
    ]