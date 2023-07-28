from django.contrib.auth.decorators import login_required
from .models import (Products, Materials)
from django.http import HttpResponse
from django.shortcuts import render
from openpyxl import Workbook


@login_required
def product_list_export_to_excel(request):
    if request.user.category == 4:
        list = Products.objects.all().order_by("product_date")
    elif request.user.category == 3:
        list = Products.objects.all().order_by("product_date")
    elif request.user.category == 2:
        list = Products.objects.filter(product_location = 'انبار مغازه غدیر').order_by('product_date')
    elif request.user.category == 1:
        list = Products.objects.filter(product_location = 'انبار پلاک سه').order_by('product_date')
    elif request.user.category == 0:
        list = Products.objects.filter(product_location = 'انبار اخلاقی').order_by('product_date')
    else:
        list = Products.objects.all().order_by("product_date")
    wb = Workbook()
    ws = wb.active
    ws.append(["ردیف", "اقدام کننده", "نام محصول", "کد محصول", "رنگ محصول", "موجودی محصول", "انبار محصول", "سالن انبار محصول", "واحد محصول", "تاریخ ایجاد محصول", "فعال/غیرفعال", "موجود/ناموجود"])
    for data in list:
        ws.append([data.row, data.product_author, data.product_name, data.product_code, data.product_color, data.product_quantity, data.product_location, data.product_hall, data.product_unit, data.jpub(), data.is_active, data.is_available])
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=Products_lists.xlsx"
    wb.save(response)
    return response


@login_required
def material_list_export_to_excel(request):
    if request.user.category == 4:
        list = Materials.objects.all().order_by("material_date")
    elif request.user.category == 3:
        list = Materials.objects.all().order_by("material_date")
    elif request.user.category == 2:
        list = Materials.objects.filter(material_location = 'انبار مغازه غدیر').order_by('material_date')
    elif request.user.category == 1:
        list = Materials.objects.filter(material_location = 'انبار پلاک سه').order_by('material_date')
    elif request.user.category == 0:
        list = Materials.objects.filter(material_location = 'انبار اخلاقی').order_by('material_date')
    else:
        list = Materials.objects.all().order_by("material_date")
    wb = Workbook()
    ws = wb.active
    ws.append(["ردیف", "اقدام کننده", "نام محصول", "کد محصول", "رنگ محصول", "موجودی محصول", "انبار محصول", "سالن انبار محصول", "واحد محصول", "تاریخ ایجاد محصول", "فعال/غیرفعال", "موجود/ناموجود"])
    for data in list:
        ws.append([data.row, data.material_author, data.material_name, data.material_code, data.material_color, data.material_quantity, data.material_location, data.material_hall, data.material_unit, data.jpub(), data.is_active, data.is_available])
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=Products_lists.xlsx"
    wb.save(response)
    return response

@login_required
def product_list_pdf(request):
    if request.user.category == 4:
        list = Products.objects.all().order_by("product_date")
    elif request.user.category == 3:
        list = Products.objects.all().order_by("product_date")
    elif request.user.category == 2:
        list = Products.objects.filter(product_location = 'انبار مغازه غدیر').order_by('product_date')
    elif request.user.category == 1:
        list = Products.objects.filter(product_location = 'انبار پلاک سه').order_by('product_date')
    elif request.user.category == 0:
        list = Products.objects.filter(product_location = 'انبار اخلاقی').order_by('product_date')
    else:
        list = Products.objects.all().order_by("product_date")
    context = {'title' : 'Products list', 'list' : list}
    return render(request, 'utils/print_product_list.html', context)


@login_required
def material_list_pdf(request):
    if request.user.category == 4:
        list = Materials.objects.all().order_by("material_date")
    elif request.user.category == 3:
        list = Materials.objects.all().order_by("material_date")
    elif request.user.category == 2:
        list = Materials.objects.filter(material_location = 'انبار مغازه غدیر').order_by('material_date')
    elif request.user.category == 1:
        list = Materials.objects.filter(material_location = 'انبار پلاک سه').order_by('material_date')
    elif request.user.category == 0:
        list = Materials.objects.filter(material_location = 'انبار اخلاقی').order_by('material_date')
    else:
        list = Materials.objects.all().order_by("material_date")
    context = {'title' : 'Materials list', 'list' : list}
    return render(request, 'utils/print_material_list.html', context)