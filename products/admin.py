from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django_admin_filter.filters import CustomFilter
from .admin_filter import  ProductAdminFilter
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'sale', 'arrived_at', 'price', 'stock']
    # list_filter = [CustomFilter]
    list_filter = [CustomFilter]


    class Meta:
        model = Product


class CategoryAdmin(MPTTModelAdmin):
    mptt_indent_field = "name"
    mptt_level_indent = 20
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
