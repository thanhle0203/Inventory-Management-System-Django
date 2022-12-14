from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'DjangoIntentory Dashboard'
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Staff', 'Order quantity')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)


admin.site.unregister(Group)