from inventory.models import (Products, Materials)
from django import forms
from attr import fields


class PRODUCTS_IMPORT_EXCEL(forms.Form):
    class Meta:
        model = Products
        fields = '__all__'


class MATERIALS_IMPORT_EXCEL(forms.Form):
    class Meta:
        model = Materials
        fields = '__all__'