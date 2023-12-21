from django.db import models
from django.urls import reverse
from django.shortcuts import render
from django.db import models
from django.contrib.sessions.models import Session
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

'''Модель продукта'''
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    srok = models.CharField(max_length=150, blank=True, verbose_name='Cрок поставки')
    description = RichTextUploadingField(blank=True, verbose_name="описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    pop_prodaj = models.BooleanField(default=False, verbose_name="популярные товары")

    def __str__(self):
        return self.name or str(self.id)

    class Meta:
        ordering = ['name']
        index_together = [          
            ['id', 'slug']          
        ]  
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @property
    def ct_models(self):
        return self._meta.model_name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])
    
'''Модель под бренд'''
class Pod_Brend(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="брент")
    image = models.ImageField(upload_to='подбрент', blank=True, verbose_name='подбренд')
    product = models.ManyToManyField(Product, verbose_name='продукт')

    class Meta:
        verbose_name = 'Под бренд'
        verbose_name_plural = 'Под бренд'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('products', args=[self.id]) 

'''Модель бренд'''
class Brend(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="брент")
    image = models.ImageField(upload_to='brends', blank=True, verbose_name='картинка бренда на главной стр')
    pod_brend = models.ManyToManyField(Pod_Brend, verbose_name='под бренд')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('pod_brand',
                        args=[self.id])    
    
'''Модель связи'''
class ProductRelation(models.Model):
    brend = models.ForeignKey('Brend', on_delete=models.CASCADE)
    pod_brend = models.ForeignKey('Pod_Brend', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связь продукта, бренда и подбренда'
        verbose_name_plural = 'Связи продуктов, брендов и подбрендов'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.product.id)])

'''Модель дом'''
class Home(models.Model):
    title_home = models.CharField(max_length=200, verbose_name='домашняя')
    product = models.ManyToManyField(Product, verbose_name='товар', related_name='homes')

    class Meta:
        verbose_name = 'домашняя'
        verbose_name_plural = 'домашняя'

    def __str__(self):
        return self.title_home

# Модель социальные иконки шапка
class Network(models.Model):
    title_ikons = models.CharField(max_length=500, verbose_name='иконка соцсети')
    network_image = models.ImageField(upload_to='network_image', blank=True, verbose_name='картинка соцсети')
    url_network = models.TextField(blank=True, verbose_name='ссылка')

    class Meta:
        verbose_name = 'социальные сети'
        verbose_name_plural = 'социальные сети'

    def __str__(self):
        return self.title_ikons
    
 # Модель контактов   
class Contact(models.Model):
    title_contact = models.CharField(max_length=200, verbose_name='контакт')
    body_contact = models.TextField(blank=True, default='', verbose_name='текст контакта')
    adress_one_contact = models.TextField(blank=True, default='', verbose_name='адрес')
    tel = models.CharField(max_length=200, verbose_name='телефон')
    web = models.TextField(blank=True, default='', verbose_name='email')
    network_ikons = models.ManyToManyField(Network, blank=True, default='', verbose_name='иконки соцсетей')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return self.title_contact
    
#Модель формы обратной связи на странице контакты
class FormObratZvonot(models.Model):
    name = models.CharField(max_length=300, verbose_name="имя")
    body = models.TextField(verbose_name='текст')

    class Meta:
        verbose_name = 'обратный звонок'
        verbose_name_plural = 'обратный звонок'

# Модель часто задаваемых воросов
class Question(models.Model):
    title_question = models.CharField(max_length=500, verbose_name='вопрос')
    body_question = models.TextField(blank=True, default='', verbose_name='ответ')

    class Meta:
        verbose_name = 'вопросы'
        verbose_name_plural = 'вопросы на странице о нас'

    def __str__(self):
        return self.title_question

# Модель О Нас
class Onas(models.Model):
    title_onas1 = models.CharField(max_length=500, verbose_name='заголовок')
    title_onas2 = models.CharField(blank=True, max_length=500, verbose_name='второй заголовок')
    body_onas = models.TextField(blank=True, default='', verbose_name='текст')
    image_uslugi = models.ImageField(upload_to='home', blank=True, verbose_name='главное фото')
    question = models.ManyToManyField(Question, verbose_name='вопрос')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'о нас'

    def __str__(self):
        return self.title_onas1
    
#Модель титл
class Setting(models.Model):
    objects = None
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir')
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
    

