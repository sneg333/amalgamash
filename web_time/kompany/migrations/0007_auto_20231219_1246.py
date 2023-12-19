# Generated by Django 3.2.23 on 2023-12-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0006_product_srok'),
    ]

    operations = [
        migrations.AddField(
            model_name='brend',
            name='image',
            field=models.ImageField(blank=True, upload_to='brends', verbose_name='картинка бренда на главной стр'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
    ]