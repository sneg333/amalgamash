# Generated by Django 3.2.12 on 2023-10-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onas',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'о нас'},
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_home', models.CharField(max_length=200, verbose_name='домашняя')),
                ('product', models.ManyToManyField(related_name='homes', to='polls.Product', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'домашняя',
                'verbose_name_plural': 'домашняя',
            },
        ),
    ]