from django.contrib import admin
from .models import *

'''Модель дом'''
admin.site.register(Home)

'''Модель Contact'''
admin.site.register(Contact)

'''Модель вопросы'''
admin.site.register(Question)

'''Модель о нас '''
admin.site.register(Onas)

'''Модель соцсети'''
admin.site.register(Network)

'''Модель Setting'''
admin.site.register(Setting)

class FormObratZvonotAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']

admin.site.register(FormObratZvonot, FormObratZvonotAdmin)

'''Модель Title'''
admin.site.register(Brend)

'''Модель Pod_Brend'''
admin.site.register(Pod_Brend)

'''Модель товара'''
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'price', 'stock', 'available']
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)
