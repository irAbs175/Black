from django.contrib.auth.decorators import login_required
from .models import (Products, Materials)
from django.http import HttpResponse
from django.shortcuts import render
from openpyxl import Workbook


@login_required
def product_list_export_to_excel(request):
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
    list = Materials.objects.all().order_by("material_date")
    wb = Workbook()
    ws = wb.active
    ws.append(["ردیف", "اقدام کننده", "نام ماده اولیه", "کد ماده اولیه", "رنگ ماده اولیه", "موجودی ماده اولیه", "انبار ماده اولیه", "سالن انبار ماده اولیه", "واحد ماده اولیه", "تاریخ ایجاد ماده اولیه", "فعال/غیرفعال", "موجود/ناموجود"])
    for data in list:
        ws.append([data.row, data.material_author, data.material_name, data.material_code, data.material_color, data.material_quantity, data.material_location, data.material_hall, data.material_unit, data.jpub(), data.is_active, data.is_available])
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=materials_lists.xlsx"
    wb.save(response)
    return response

@login_required
def product_list_pdf(request):
    list = Products.objects.all().order_by("product_date")
    context = {'title' : 'Products list', 'list' : list}
    return render(request, 'utils/print_product_list.html', context)


@login_required
def material_list_pdf(request):
    list = Materials.objects.all().order_by("material_date")
    context = {'title' : 'Materials list', 'list' : list}
    return render(request, 'utils/print_material_list.html', context)