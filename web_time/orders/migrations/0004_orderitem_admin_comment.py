# Generated by Django 3.2.12 on 2023-10-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='admin_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]