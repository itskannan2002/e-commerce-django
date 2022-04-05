
from django.contrib import admin
from .models import Product
from .models import Variation


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')

    list_editable = ('is_active',) 
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')



admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)