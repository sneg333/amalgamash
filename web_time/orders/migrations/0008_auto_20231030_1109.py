# Generated by Django 3.2.12 on 2023-10-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('orders', '0007_remove_order_paid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Заказанный товар', 'verbose_name_plural': 'Заказанный товар'},
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.CharField(choices=[('not_done', 'Не исполнено'), ('in_progress', 'Взят в работу'), ('done', 'Исполнено')], default='not_done', max_length=250, verbose_name='статус заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(blank=True, related_name='заказы_ы', to='cart.CartItem'),
        ),
    ]
