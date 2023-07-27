from .serializers import (ProductsSerializer, MaterialsSerializer, ProductsCardexSerializer, MaterialsCardexsSerializer)
from .models import (Products, Materials, ProductsCardex, MaterialsCardex)
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, filters
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from .split import split_lhcc as getData
from reportlab.pdfbase import pdfmetrics
from django.shortcuts import render
from reportlab.lib import colors
from root.local import BASE_DIR
from openpyxl import Workbook
import pandas as pd
import os


''' Create rest api views '''
class ProductsViewSet(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    ordering_fields = ['product_author', 'product_name', 'product_code', 'product_color', 'product_quantity', 'product_location', 'product_hall', 'product_unit', 'product_date', 'is_active', 'is_available',]
    search_fields = ['product_code', 'product_name']
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class MaterialsViewSet(generics.ListCreateAPIView):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    ordering_fields = ['material_author', 'material_name', 'material_code', 'material_color', 'material_quantity', 'material_location', 'material_hall', 'material_unit', 'material_date', 'is_active', 'is_available',]
    search_fields = ['material_code', 'material_name']
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class ProductsCardexViewSet(generics.ListCreateAPIView):
    queryset = ProductsCardex.objects.all()
    serializer_class = ProductsCardexSerializer
    ordering_fields = ['row', 'author', 'product', 'factor_number', 'number', 'description', 'operation', 'date', 'status', 'quantity', 'factor_row']
    search_fields = ['product', 'factor_number',]
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class MaterialsCardexsViewSet(generics.ListCreateAPIView):
    queryset = MaterialsCardex.objects.all()
    serializer_class = MaterialsCardexsSerializer
    ordering_fields = ['row', 'author', 'material', 'factor_number', 'number', 'description', 'operation', 'date', 'status', 'quantity', 'factor_row']
    search_fields = ['material', 'factor_number',]
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


''' Render pages '''
@login_required
def materials(request):
    if request.user.category == 4:
        materials = Materials.objects.all().order_by('-material_date')
    elif request.user.category == 3:
        materials = Materials.objects.all().order_by('-material_date')
    elif request.user.category == 2:
        materials = Materials.objects.filter(material_location = 'انبار مغازه غدیر').order_by('-material_date')
    elif request.user.category == 1:
        materials = Materials.objects.filter(material_location = 'انبار پلاک سه').order_by('-material_date')
    elif request.user.category == 0:
        materials = Materials.objects.filter(material_location = 'انبار اخلاقی').order_by('-material_date')
    return render(request, "inventory/materials/materials.html", {'materials' : materials})

@login_required
def add_materials(request):
    return render(request, "inventory/materials/add_materials.html")

@login_required
def products(request):
    if request.user.category == 4 :
        products = Products.objects.all().order_by('-product_date')
    elif request.user.category == 3 :
        products = Products.objects.all().order_by('-product_date')
    elif request.user.category == 2:
        products = Products.objects.filter(product_location = 'انبار مغازه غدیر').order_by('-product_date')
    elif request.user.category == 1:
        products = Products.objects.filter(product_location = 'انبار پلاک سه').order_by('-product_date')
    elif request.user.category == 0:
        products = Products.objects.filter(product_location = 'انبار اخلاقی').order_by('-product_date')
    return render(request, "inventory/products/products.html", {'products' : products})

@login_required
def add_products(request):
    return render(request, "inventory/products/add_products.html")

@login_required
def add_products_cardex(request, location__code__color):
    location, code, color = getData(location__code__color)
    key = {'location':location,'code': code, 'color':color}
    product = Products.objects.filter(product_location = location, product_code = code, product_color = color)
    if product.exists():
        cardex = ProductsCardex.objects.filter(product = code, public_key = f'{location}{code}{color}').order_by('-date')
        count = cardex.count()
        context = {'product' : product, 'cardex' : cardex, 'key' : key, 'count' : count}
        return render(request, "inventory/products/add_cardex.html", context)
    else:
        return render(request, "dashboard/dashboard.html")

@login_required
def add_materials_cardex(request, location__code__color):
    location, code, color = getData(location__code__color)
    key = {'location':location,'code': code, 'color':color}
    material = Materials.objects.filter(material_location = location, material_code = code, material_color = color)
    if material.exists():
        cardex = MaterialsCardex.objects.filter(material = code, public_key = f'{location}{code}{color}').order_by('-date')
        context = {'material' : material, 'cardex' : cardex, 'key' : key}
        return render(request, "inventory/materials/add_cardex.html", context)
    else:
        return render(request, "dashboard/dashboard.html")

@login_required
def inventory(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def product_cardex_export_to_excel(request, location__code__color):
    location, code, color = getData(location__code__color)
    lcc = f'{location}{code}{color}'
    row = 1
    cardex = ProductsCardex.objects.filter(public_key = lcc).order_by("date")
    wb = Workbook()
    ws = wb.active
    ws.append(["ردیف", "تاریخ", "شماره حواله/فاکتور", "ردیف فاکتور", "شرح اقدامات", "ورودی", "خروجی", "موجودی", "اقدام کننده",])
    for data in cardex:
        if data.status:
            ws.append([row, data.jpub(), data.factor_number, data.factor_row, data.description, data.number, "0", data.quantity, data.author])
            row += 1
        else:
            ws.append([row, data.jpub(), data.factor_number, data.factor_row, data.description, "0", data.number, data.quantity, data.author])
            row +=1 
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=cardex-{code}.xlsx"
    wb.save(response)
    return response

@login_required
def material_cardex_export_to_excel(request, location__code__color):
    location, code, color = getData(location__code__color)
    lcc = f'{location}{code}{color}'
    cardex = MaterialsCardex.objects.filter(public_key = lcc).order_by("date")
    row = 1
    wb = Workbook()
    ws = wb.active
    ws.append(["ردیف", "تاریخ", "شماره حواله/فاکتور","ردیف فاکتور", "شرح اقدامات", "ورودی", "خروجی", "موجودی", "اقدام کننده",])
    for data in cardex:
        if data.status:
            ws.append([row, data.jpub(), data.factor_number, data.factor_row, data.description, data.number, "0", data.quantity, data.author])
            row += 1
        else:
            ws.append([row, data.jpub(), data.factor_number, data.factor_row, data.description, "0", data.number, data.quantity, data.author])
            row += 1
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=cardex-{code}.xlsx"
    wb.save(response)
    return response

@login_required
def product_cardex_export_to_pdf(request, location__code__color):
    location, code, color = getData(location__code__color)
    lcc = f'{location}{code}{color}'
    product = Products.objects.filter(product_location = location, product_code = code, product_color = color).order_by("product_date")
    if product.exists():
        cardex = ProductsCardex.objects.filter(public_key = lcc).order_by("date")
        context = {'code' : code, 'product': product, 'cardex': cardex}
        return render(request, "utils/print_product.html", context)
    else:
        return render(request, "dashboard/dashboard.html")

@login_required
def material_cardex_export_to_pdf(request, location__code__color):
    location, code, color = getData(location__code__color)
    lcc = f'{location}{code}{color}'
    material = Materials.objects.filter(material_location = location, material_code = code, material_color = color).order_by("material_date")
    if material.exists():
        cardex = MaterialsCardex.objects.filter(public_key = lcc).order_by("date")
        context = {'code' : code, 'material': material, 'cardex': cardex}
        return render(request, "utils/print_material.html", context)
    else:
        return render(request, "dashboard/dashboard.html")
