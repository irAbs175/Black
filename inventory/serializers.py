from .models import Products, Materials, ProductsCardex, MaterialsCardex
from rest_framework import serializers


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['product_author', 'product_name', 'product_code', 'product_color', 'product_quantity', 'product_location', 'product_hall', 'product_unit', 'product_date', 'is_active', 'is_available',]


class MaterialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materials
        fields = ['material_author', 'material_name', 'material_code', 'material_color', 'material_quantity', 'material_location', 'material_hall', 'material_unit', 'material_date', 'is_active', 'is_available',]


class ProductsCardexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductsCardex
        fields = ['row', 'author', 'product', 'factor_number', 'number', 'description', 'operation', 'date', 'status', 'quantity', 'factor_row']


class MaterialsCardexsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaterialsCardex
        fields = ['row', 'author', 'material', 'factor_number', 'number', 'description', 'operation', 'date', 'status', 'quantity', 'factor_row']