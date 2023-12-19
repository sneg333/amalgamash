from django.contrib import admin
from .models import Order, OrderItem

# товар из корзины внутри вкладки Заказы
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Количество пустых форм для заполнения
    raw_id_fields = ['product']
    
'''заказы'''
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email',
                    'address', 'tel', 'paid',
                    'created', 'updated']
    search_fields = ['id', 'tel']
    list_filter = [ 'created', 'updated', 'paid']
    exclude = ('cart_items',)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)


'''заказанный товар'''
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product', 'quantity', 'price', 'id', 'admin_comment']

    def order_id(self, obj):
        return obj.order.id

admin.site.register(OrderItem, OrderItemAdmin)

