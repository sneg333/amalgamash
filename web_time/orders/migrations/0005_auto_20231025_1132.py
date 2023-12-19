# Generated by Django 3.2.12 on 2023-10-25 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0006_product_srok'),
        ('orders', '0004_orderitem_admin_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='admin_comment',
            field=models.TextField(blank=True, null=True, verbose_name='комментарий администратора'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='kompany.product', verbose_name='ID товара'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='количество'),
        ),
    ]