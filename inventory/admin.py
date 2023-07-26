from .models import Products, Materials, ProductsCardex, MaterialsCardex
from django.contrib import admin


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'product_name', 'product_location', 'product_hall', 'product_quantity', 'product_unit', 'product_author',)
    list_filter = ('product_author', 'product_location', 'product_hall', 'product_date', 'is_active', 'is_available', 'product_unit',)
    search_fields = ('product_code', 'product_name',)


admin.site.register(Products, ProductsAdmin)

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('material_code', 'material_name', 'material_location', 'material_hall', 'material_quantity', 'material_unit', 'material_author',)
    list_filter = ('material_author', 'material_location', 'material_hall', 'material_date', 'is_active', 'is_available', 'material_unit',)
    search_fields = ('material_code', 'material_name',)


admin.site.register(Materials, MaterialsAdmin)

class ProductsCardexAdmin(admin.ModelAdmin):
    list_display = ('factor_number', 'product', 'operation', 'number', 'author',)
    list_filter = ('author', 'date', 'operation',)
    search_fields = ('factor_number',  'product',)


admin.site.register(ProductsCardex, ProductsCardexAdmin)

class MaterialsCardexAdmin(admin.ModelAdmin):
    list_display = ('factor_number', 'material', 'operation', 'number', 'author',)
    list_filter = ('author', 'date', 'operation',)
    search_fields = ('factor_number',  'material',)


admin.site.register(MaterialsCardex, MaterialsCardexAdmin)