from django.shortcuts import render, redirect
from django.db.models import Sum, F
from django.conf import settings
from django.core.mail import send_mail
from .models import OrderItem, Order
from kompany.models import Brend, Contact, Network
from .forms import OrderCreateForm
from cart.models import Cart, CartItem
from cart.views import _cart_id
from kompany.utils import get_constanta

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def order_create(request):    
    # Получаем корзину текущего пользователя
    cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)  # Получаем все активные товары в корзине

    if request.method == 'POST':
        # Если запрос является POST-запросом (например, форма была отправлена), обрабатываем его.
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Если форма прошла валидацию, создаем объект заказа, но не сохраняем его в базе данных пока.
            order = form.save(commit=False)
            #вычисляем итоговую сумму заказа
            total_price = cart_items.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price'] or 0
            #вычисляем количество товаров в заказе
            total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
            # Теперь сохраняем заказ в базе данных.
            order.save()
            
            # Создаем OrderItem для каждого элемента корзины
            order_items = []

            for cart_item in cart_items:
                order_item = OrderItem(
                    order=order,
                    product=cart_item.product,
                    price=cart_item.product.price,
                    quantity=cart_item.quantity,
                )
                order_item.save()

                # Добавляем информацию о товаре в список заказанных товаров
                order_items.append({
                    'product': order_item.product,
                    'quantity': order_item.quantity,
                    'subtotal': order_item.get_cost,  # Используем метод sub_total
                })

            #уведомление администратора на почту
            # subject = f'Новый заказ #{order.id}'
            # message = f'Поступил новый заказ #{order.id}. Пожалуйста, проверьте админ-панель.'
            # from_email = settings.DEFAULT_FROM_EMAIL
            # admin_email = ['admin@admin.ru']
            # send_mail(subject, message, from_email, admin_email)

            # Очищаем корзину
            cart.clear()

            context = {
                'form': form,
                'order_items': order_items,
                'total_price': total_price,
                'total_quantity': total_quantity,
                **get_constanta(),
            }
            return redirect('created')
    else:
        # Если запрос не является POST-запросом (например, пользователь только открыл страницу), создаем пустую форму.
        form = OrderCreateForm()
        total_price = cart_items.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price'] or 0
        total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        context = {
            'form': form,
            'cart_items': cart_items,  # Передаем данные о товарах в корзине
            'total_price': total_price,
            'total_quantity': total_quantity,
            **get_constanta(),
        }

    return render(request, 'orders/create.html', context)

def created(request):
    last_order = Order.objects.latest('created') 

    context = {
        'last_order_id': last_order.id,
        **get_constanta(),
    }
    return render(request, 'orders/created.html', context)

