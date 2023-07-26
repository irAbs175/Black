from .extensions.jalali_converter import jalali_converter as jConvert, cardex_jalali_converter
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db.models import F
from django.db import models


class Products(models.Model):
    product_author = models.CharField(max_length=40, verbose_name='اپراتور ثبت',null=False, blank=False )
    product_name = models.CharField(max_length=300, verbose_name='نام کالا',null=False, blank=False )
    product_code = models.CharField(max_length=50, verbose_name='کد کالا',null=False, blank=False )
    product_color = models.CharField(max_length=50, verbose_name='رنگ کالا',null=False, blank=False )
    product_quantity = models.PositiveIntegerField(verbose_name='موجودی کالا', null=True)
    product_location = models.CharField(max_length=50, verbose_name='انبار کالا',null=False, blank=False )
    product_hall = models.CharField(max_length=20, verbose_name='سالن انبار کالا',null=False, blank=False )
    product_unit = models.CharField(max_length=20, verbose_name='واحد',null=False, blank=False )
    product_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان دقیق ثبت', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال', blank=False, null=False)
    is_available = models.BooleanField(default=True, verbose_name='موجودی / عدم موجودی', blank=False, null=False)
    row = models.PositiveIntegerField(default=0)

    objects = models.Manager()

    def jpub(self):
        return jConvert(self.product_date)

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'


class ProductsCardex(models.Model):
    author = models.CharField(max_length=40, verbose_name='اپراتور ثبت',null=False, blank=False )
    product = models.CharField(max_length=50, verbose_name='کالا',null=False, blank=False )
    factor_number = models.CharField(max_length=50, verbose_name='شماره فاکتور',null=False, blank=False )
    factor_row = models.CharField(max_length=50, verbose_name='ردیف فاکتور',null=False, blank=False )
    number = models.PositiveIntegerField(verbose_name='تعداد', null=True)
    description = models.CharField(max_length=300, verbose_name='شرح عملیات',null=False, blank=False )
    operation = models.CharField(max_length=20, verbose_name='عملیات',null=False, blank=False )
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت', null=True, blank=True)
    status = models.BooleanField(verbose_name='ورودی / خروجی', blank=True, null=True)
    quantity = models.PositiveIntegerField(null=True)
    row = models.PositiveIntegerField(default=0)

    def jpub(self):
        return cardex_jalali_converter(self.date)

    class Meta:
        verbose_name = 'کاردکس'
        verbose_name_plural = 'کاردکس کالاها'


class Materials(models.Model):
    material_author = models.CharField(max_length=40, verbose_name='اپراتور ثبت',null=False, blank=False )
    material_name = models.CharField(max_length=300, verbose_name='نام',null=False, blank=False )
    material_code = models.CharField(max_length=50, verbose_name='کد',null=False, blank=False )
    material_color = models.CharField(max_length=50, verbose_name='رنگ',null=False, blank=False )
    material_quantity = models.PositiveIntegerField(verbose_name='موجودی', null=True)
    material_location = models.CharField(max_length=50, verbose_name='انبار',null=False, blank=False )
    material_hall = models.CharField(max_length=20, verbose_name='سالن انبار',null=False, blank=False )
    material_unit = models.CharField(max_length=20, verbose_name='واحد',null=False, blank=False )
    material_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان دقیق ثبت', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال', blank=False, null=False)
    is_available = models.BooleanField(default=True, verbose_name='موجودی / عدم موجودی', blank=False, null=False)
    row = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    
    def jpub(self):
        return jConvert(self.material_date)

    class Meta:
        verbose_name = 'ماده اولیه'
        verbose_name_plural = 'مواد اولیه'


class MaterialsCardex(models.Model):
    author = models.CharField(max_length=40, verbose_name='اپراتور ثبت',null=False, blank=False )
    material = models.CharField(max_length=50, verbose_name='ماده اولیه',null=False, blank=False )
    factor_number = models.CharField(max_length=50, verbose_name='شماره فاکتور',null=False, blank=False )
    factor_row = models.CharField(max_length=50, verbose_name='ردیف فاکتور',null=False, blank=False )
    number = models.PositiveIntegerField(verbose_name='تعداد', null=True)
    description = models.CharField(max_length=300, verbose_name='شرح عملیات',null=False, blank=False )
    operation = models.CharField(max_length=20, verbose_name='عملیات',null=False, blank=False )
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت', null=True, blank=True)
    status = models.BooleanField(verbose_name='ورودی / خروجی', blank=True, null=True)
    quantity = models.PositiveIntegerField(null=True)
    row = models.PositiveIntegerField(default=0)

    def jpub(self):
        return cardex_jalali_converter(self.date)

    class Meta:
        verbose_name = 'کاردکس'
        verbose_name_plural = 'کاردکس مواد اولیه'

# Function to update row numbers
def update_row_numbers(sender, instance, **kwargs):
    if kwargs.get('created'):
        # New record is being created
        last_row = sender.objects.all().order_by('-row').first()
        if last_row:
            instance.row = last_row.row + 1
        else:
            instance.row = 1
        instance.save()

# Function to update row numbers after deletion
def update_row_numbers_on_delete(sender, instance, **kwargs):
    # Get the deleted row number
    deleted_row_number = instance.row
    # Update row numbers for records below the deleted row
    sender.objects.filter(row__gt=deleted_row_number).update(row=F('row') - 1)

# Connect the signals to the model
post_save.connect(update_row_numbers, sender=ProductsCardex)
pre_delete.connect(update_row_numbers_on_delete, sender=ProductsCardex)
post_save.connect(update_row_numbers, sender=MaterialsCardex)
pre_delete.connect(update_row_numbers_on_delete, sender=MaterialsCardex)
post_save.connect(update_row_numbers, sender=Products)
pre_delete.connect(update_row_numbers_on_delete, sender=Products)
post_save.connect(update_row_numbers, sender=Materials)
pre_delete.connect(update_row_numbers_on_delete, sender=Materials)