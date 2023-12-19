from django.db import models
from decimal import Decimal
from django.urls import reverse
from kompany.models import Product

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        db_table = 'Cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'корзина'

    def get_absolute_url(self):
        return reverse('products',
                        args=[self.id])
    
    def clear(self):
        self.cartitem_set.all().delete()

    def calculate_total(self):
        return sum(item.sub_total() for item in self.cartitem_set.filter(active=True))
    
    def calculate_counter(self):
        return sum(item.quantity for item in self.cartitem_set.filter(active=True))
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #связываем товар в корзине с конкретным продуктом
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #связываем товар в корзине с конкретной корзиной
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'товар в корзине'

    def sub_total(self):
        return self.product.price * self.quantity
    
    def get_total_price(self):
        return Decimal(self.product.price) * self.quantity
    
    def __str__(self): # отображение в админ панели
        return f"{self.product.name} ({self.quantity})"

