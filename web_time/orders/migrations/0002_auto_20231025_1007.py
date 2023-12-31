# Generated by Django 3.2.12 on 2023-10-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tel',
            field=models.CharField(max_length=100, verbose_name='контактный телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='дата изменения'),
        ),
    ]
