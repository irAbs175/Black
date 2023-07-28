from inventory.models import (Products, Materials, ProductsCardex, MaterialsCardex)
from .forms import (PRODUCTS_IMPORT_EXCEL, MATERIALS_IMPORT_EXCEL)
from .resources import (ProductsResource, MaterialsResource)
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from inventory.models import (Products, Materials)
from django.shortcuts import render
from django.db import transaction
from tablib import Dataset
import pandas as pd
import csv
import os
import io



@login_required
def index(request):
        return render(request, "dashboard/dashboard.html")

@login_required
def search(request, search):
    cat = request.user.category
    if cat == 4:
        if Products.objects.filter(product_code__contains = search).exists():
            products = Products.objects.filter(product_code__contains = search).order_by('-product_date')
        elif Materials.objects.filter(material_code__contains = search).exists():
            products = Materials.objects.filter(material_code__contains = search).order_by('-material_date')
        else:
            products = Products.objects.filter(product_code__contains = search).order_by('-product_date')
    elif cat == 3:
        if Products.objects.filter(product_code__contains = search).exists():
            products = Products.objects.filter(product_code__contains = search).order_by('-product_date')
        elif Materials.objects.filter(material_code__contains = search).exists():
            products = Materials.objects.filter(material_code__contains = search).order_by('-material_date')
        else:
            products = Products.objects.filter(product_code__contains = search).order_by('-product_date')
    elif cat == 2:
        if Products.objects.filter(product_location = 'انبار مغازه غدیر', product_code__contains = search).exists():
            products = Products.objects.filter(product_location = 'انبار مغازه غدیر', product_code__contains = search).order_by('-product_date')
        elif Materials.objects.filter(material_location = 'انبار مغازه غدیر', material_code__contains = search).exists():
            products = Materials.objects.filter(material_location = 'انبار مغازه غدیر', material_code__contains = search).order_by('-material_date')
        else:
            products = Products.objects.filter(product_location = 'انبار مغازه غدیر', product_code__contains = search).order_by('-product_date')
    elif cat == 1:
        if Products.objects.filter(product_location = 'انبار پلاک سه', product_code__contains = search).exists():
            products = Products.objects.filter(product_location = 'انبار پلاک سه', product_code__contains = search).order_by('-product_date')
        elif Materials.objects.filter(material_location = 'انبار پلاک سه', material_code__contains = search).exists():
            products = Materials.objects.filter(material_location = 'انبار پلاک سه', material_code__contains = search).order_by('-material_date')
        else:
            products = Products.objects.filter(product_location = 'انبار پلاک سه', product_code__contains = search).order_by('-product_date')
    elif cat == 0:
        if Products.objects.filter(product_location = 'انبار اخلاقی', product_code__contains = search).exists():
            products = Products.objects.filter(product_location = 'انبار اخلاقی', product_code__contains = search).order_by('-product_date')
        elif Materials.objects.filter(material_location = 'انبار اخلاقی', material_code__contains = search).exists():
            products = Materials.objects.filter(material_location = 'انبار اخلاقی', material_code__contains = search).order_by('-material_date')
        else:
            products = Products.objects.filter(product_code__contains = search).order_by('-product_date')
    return render(request, "utils/search.html", {'products': products})

@login_required
def import_excel(request):
    context = {'status':''}
    if request.method == 'POST':
        if request.POST.get('mode') == 'محصولات':
            print(request.POST.get('mode'))
            excel_resource = PRODUCTS_IMPORT_EXCEL()
            dataset = Dataset()
            new_excel = request.FILES['myfile']
            imported_data = dataset.load(new_excel.read(), format='xlsx')
            for data in imported_data :
                value = Products(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                    data[9],
                    data[10]
                )
                value.save()
                context['status'] = 'درون ریزی محصول با موفقیت انجام شد' 
        elif request.POST.get('mode') == 'مواد اولیه':
            excel_resource = MATERIALS_IMPORT_EXCEL()
            dataset = Dataset()
            new_excel = request.FILES['myfile']
            imported_data = dataset.load(new_excel.read(), format='xlsx')
            for data in imported_data :
                value = Materials(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                    data[9],
                    data[10]
                )
                value.save()
                context['status'] = 'فایل با موفقیت درون ریزی شد' 
        else:
            context['status'] = 'حالت درون ریزی را وارد کنید' 
    return render(request, 'utils/import_excel.html', context)