from django import forms
from .models import Order
from cart.models import CartItem

class OrderCreateForm(forms.ModelForm):
    cart_items = forms.ModelMultipleChoiceField(
        queryset=CartItem.objects.all(),
        widget=forms.HiddenInput,
        required=False,
    )
    
    class Meta:
        model = Order
        fields = ['first_name', 'tel', 'email', 'address']
        labels = {
            'first_name': 'Имя',
            'tel': 'контактный телефон',
            'email': 'email',
            'address': 'Адрес доставки',
        }