from django.contrib import admin

# Register your models here.
from CBVIApp.models import Product,Cart
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['pid','pname','category','price','description']
admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=['pid','quantity','user']
admin.site.register(Cart,CartAdmin)
