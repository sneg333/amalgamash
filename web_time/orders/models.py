from django.db import models
from decimal import Decimal
from kompany.models import Product
from cart.models import CartItem

# Модель заказа
class Order(models.Model):
    PAID_CHOICES = [
        ('not_done', ('Не исполнено')),
        ('in_progress', ('Взят в работу')),
        ('done', ('Исполнено')),
    ]
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    address = models.CharField(max_length=250, verbose_name="Адрес доставки")
    email = models.EmailField()
    tel = models.CharField(max_length=100, verbose_name="контактный телефон")
    created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="дата изменения")
    paid = models.CharField(default='not_done', choices=PAID_CHOICES, verbose_name="статус заказа", max_length=250)

    # Связь с товарами в корзине
    cart_items = models.ManyToManyField(CartItem, related_name='заказы_ы', blank=True)  # Используем строки для отложенной загрузки модели

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.first_name} - Заказ №{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.cart_items.all())

# Модель заказа в корзине
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name="название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="количество")
    admin_comment = models.TextField(blank=True, null=True, verbose_name="комментарий администратора")

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанный товар'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
    
    def get_total_price(self):
        return Decimal(self.price) * self.quantity
    



