from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact, FormObratZvonot, Onas, Home, Product, Brend, Pod_Brend, Product
from .forms import FormObratZvonok
from .utils import get_constanta

# Страница дом
def home_page(request):
    home = Home.objects.all()
    population_products = Product.objects.filter(pop_prodaj=True, available=True)

    context = {
        'home': home,
        'population_products': population_products,
        **get_constanta(),
        }
    return render(request, 'kompany/home_page.html', context)

# О Нас 
def onas(request):
    onas = Onas.objects.all()

    context = {
        'onas': onas,
        **get_constanta(),
        }
    return render(request, 'kompany/onas.html', context)

# Страница контактов
def contact(request):
    formObratZvonok = FormObratZvonot.objects.all()

    form = FormObratZvonok()
    if request.method == "POST":
        form = FormObratZvonok(request.POST)
        if form.is_valid():
            post = FormObratZvonot()
            post.name = form.cleaned_data['name']
            post.body = form.cleaned_data['body']
            post.save()

            #уведомление на почту
            # send_mail('обратный звонок амальгама шоп',
            #            f'Имя: {post.name}\nТекст: {post.body}',
            #              settings.EMAIL_HOST_USER, 
            #              ['admin@admin.ru'])
            return HttpResponseRedirect('/contact')

    context = {
        'formObratZvonok': formObratZvonok,
        'form': form,
        **get_constanta(),
        }
    return render(request, 'kompany/contact.html', context)

# страница Под бренд
def pod_brand(request, id):
    pod_brands = get_object_or_404(Brend, id=id)

    context = {
        'pod_brands': pod_brands,
        **get_constanta(),
    }
    return render(request, 'kompany/pod_brand.html', context)

# список продуктов - таблица
def products(request, id):
    products = get_object_or_404(Pod_Brend, id=id)

    context = {
        'products': products,
        **get_constanta(),
    }
    return render(request, 'kompany/products.html', context)

# страница товара
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    context = {
        'product': product,
        **get_constanta(),
    }
    return render(request, 'kompany/product_detail.html',context)

#Поиск товара
def search_view(request):
    query = request.GET.get('q')  # Получаем запрос из параметра 'q' в GET-запросе
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()

    context = {
        'query': query,
        'products': products,
        **get_constanta(),
    }
    return render(request, 'kompany/search_results.html', context)
