from .models import (Products, Materials, ProductsCardex, MaterialsCardex)
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


''' Creare / update inventory '''
@login_required
@csrf_exempt
def js_add_products(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_code = request.POST.get('product_code')
        product_color = request.POST.get('product_color')
        product_location = request.POST.get('product_location')
        product_hall = request.POST.get('product_hall')
        product_unit = request.POST.get('product_unit')
        if product_name:
            if product_code:
                if product_color:
                    if product_location and product_location != "انتخاب محل انبار":
                        if product_hall and product_hall != "انتخاب سالن انبار":
                            if product_unit and product_unit != "انتخاب واحد شمارش":
                                if Products.objects.filter(product_name = product_name, product_code = product_code).exists():
                                    return JsonResponse({'status': 'محصول از قبل تعریف شده و موجود است', 'success': False})
                                else:
                                    full_name = request.user.first_name + " " + request.user.last_name
                                    Products.objects.create(
                                        product_author = full_name,
                                        product_name = product_name,
                                        product_code = product_code,
                                        product_color = product_color,
                                        product_quantity = 0,
                                        product_location = product_location,
                                        product_hall = product_hall,
                                        product_unit = product_unit,
                                    )
                                    return JsonResponse({'status': 'محصول با موفقیت افزوده شد', 'success':True})
                            else:
                                return JsonResponse({'status': 'واحد شمارش انتخاب نشده', 'success': False})
                        else:
                            return JsonResponse({'status': 'سالن انبار انتخاب نشده', 'success': False})
                    else:
                        return JsonResponse({'status': 'محل انبار انتخاب نشده', 'success': False})
                else:
                    return JsonResponse({'status': 'رنگ محصول را وارد کنید', 'success': False})
            else:
                return JsonResponse({'status': 'کد محصول را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status': 'نام محصول را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})

@login_required
@csrf_exempt
def js_add_materials(request):
    if request.method == 'POST':
        material_name = request.POST.get('material_name')
        material_code = request.POST.get('material_code')
        material_color = request.POST.get('material_color')
        material_location = request.POST.get('material_location')
        material_hall = request.POST.get('material_hall')
        material_unit = request.POST.get('material_unit')
        if material_name:
            if material_code:
                if material_color:
                    if material_location and material_location != "انتخاب محل انبار":
                        if material_hall and material_hall != "انتخاب سالن انبار":
                            if material_unit and material_unit != "انتخاب واحد شمارش":
                                if Materials.objects.filter(material_name = material_name, material_code = material_code).exists():
                                    return JsonResponse({'status': 'ماده اولیه از قبل تعریف شده و موجود است', 'success': False})
                                else:
                                    full_name = request.user.first_name + " " + request.user.last_name
                                    Materials.objects.create(
                                        material_author = full_name,
                                        material_name = material_name,
                                        material_code = material_code,
                                        material_color = material_color,
                                        material_quantity = 0,
                                        material_location = material_location,
                                        material_hall = material_hall,
                                        material_unit = material_unit,
                                    )
                                    return JsonResponse({'status': 'ماده اولیه با موفقیت افزوده شد', 'success':True})
                            else:
                                return JsonResponse({'status': 'واحد شمارش انتخاب نشده', 'success': False})
                        else:
                            return JsonResponse({'status': 'سالن انبار انتخاب نشده', 'success': False})
                    else:
                        return JsonResponse({'status': 'محل انبار انتخاب نشده', 'success': False})
                else:
                    return JsonResponse({'status': 'رنگ ماده اولیه را وارد کنید', 'success': False})
            else:
                return JsonResponse({'status': 'کد ماده اولیه را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status': 'نام ماده اولیه را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})

@login_required
@csrf_exempt
def js_update_products(request):
    if request.method == 'POST':
        factor_number = request.POST.get('factor_number')
        number = request.POST.get('number')
        description = request.POST.get('description')
        operation = request.POST.get('operation')
        product_code = request.POST.get('product_code')
        if factor_number:
            if number:
                if operation and operation != "انتخاب عملیات":
                    if description:
                        if product_code:
                            if Products.objects.filter(product_code = product_code).exists():
                                full_name = request.user.first_name + " " + request.user.last_name
                                product = Products.objects.filter(product_code = product_code).first()
                                if operation == "ورودی":
                                    total = product.product_quantity + int(number)
                                    product.product_quantity = total
                                    product.save()
                                    ProductsCardex.objects.create(
                                        author = full_name,
                                        product = product_code,
                                        factor_number = factor_number,
                                        number = number,
                                        description = description,
                                        operation = operation,
                                        status = True,
                                        quantity = product.product_quantity,
                                    )
                                    return JsonResponse({'status': 'کاردکس با موفقیت ایجاد و موجودی به روز شد', 'success': True})
                                elif operation == "خروجی":
                                    if product.product_quantity == 0:
                                        return JsonResponse({'status':'محصول مورد نظر فاقد موجودی است', 'success': False})
                                    else:
                                        total = product.product_quantity - int(number)
                                        product.product_quantity = total
                                        product.save()
                                        ProductsCardex.objects.create(
                                            author = full_name,
                                            product = product_code,
                                            factor_number = factor_number,
                                            number = number,
                                            description = description,
                                            operation = operation,
                                            status = False,
                                            quantity = product.product_quantity,
                                        )
                                        return JsonResponse({'status': 'کاردکس با موفقیت ایجاد شد و موجودی به روز شد', 'success': True})
                            else:
                                return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                        else:
                            return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                    else:
                        return JsonResponse({'status':'شرح عملیات را وارد کنید', 'success': False})
                else:
                    return JsonResponse({'status':'عملیات را انتخاب کنید', 'success': False})
            else:
                return JsonResponse({'status':'تعداد را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status':'شماره فاکتور را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})

@login_required
@csrf_exempt
def js_update_materials(request):
    if request.method == 'POST':
        factor_number = request.POST.get('factor_number')
        number = request.POST.get('number')
        description = request.POST.get('description')
        operation = request.POST.get('operation')
        material_code = request.POST.get('material_code')
        if factor_number:
            if number:
                if operation and operation != "انتخاب عملیات":
                    if description:
                        if material_code:
                            if Materials.objects.filter(material_code = material_code).exists():
                                full_name = request.user.first_name + " " + request.user.last_name
                                material = Materials.objects.filter(material_code = material_code).first()
                                if operation == "ورودی":
                                    total = material.material_quantity + int(number)
                                    material.material_quantity = total
                                    material.save()
                                    MaterialsCardex.objects.create(
                                        author = full_name,
                                        material = material_code,
                                        factor_number = factor_number,
                                        number = number,
                                        description = description,
                                        operation = operation,
                                        status = True,
                                        quantity = material.material_quantity,
                                    )
                                    return JsonResponse({'status': 'کاردکس با موفقیت ایجاد و موجودی به روز شد', 'success': True})
                                elif operation == "خروجی":
                                    if material.material_quantity == 0:
                                        return JsonResponse({'status':'محصول مورد نظر فاقد موجودی است', 'success': False})
                                    else:
                                        total = material.material_quantity - int(number)
                                        material.material_quantity = total
                                        material.save()
                                        MaterialsCardex.objects.create(
                                            author = full_name,
                                            material = material_code,
                                            factor_number = factor_number,
                                            number = number,
                                            description = description,
                                            operation = operation,
                                            status = False,
                                            quantity = material.material_quantity,
                                        )
                                        return JsonResponse({'status': 'کاردکس با موفقیت ایجاد شد و موجودی به روز شد', 'success': True})
                            else:
                                return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                        else:
                            return JsonResponse({'status':'ابتدا باید محصول را تعریف کنید', 'success': False})
                    else:
                        return JsonResponse({'status':'شرح عملیات را وارد کنید', 'success': False})
                else:
                    return JsonResponse({'status':'عملیات را انتخاب کنید', 'success': False})
            else:
                return JsonResponse({'status':'تعداد را وارد کنید', 'success': False})
        else:
            return JsonResponse({'status':'شماره فاکتور را وارد کنید', 'success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر', 'success': False})