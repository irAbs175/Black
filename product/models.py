from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail_color_panel.edit_handlers import NativeColorPanel
from user_accounts.models import user_accounts as User
from wagtail.snippets.models import register_snippet
from wagtail_color_panel.fields import ColorField
from django.db.models import PROTECT, SET_NULL
from wagtail.models import Page, PageManager
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from django.utils import timezone
from django.db.models import Sum
from index.models import Comment
from django.db import models
import pandas as pd


class ProductPageManager(PageManager):
    '''Inventory & Products Manager'''
    pass


@register_snippet
class ProductBrand(models.Model):
    ''' Product Brands '''
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='یک مجموعه برای برند انتخاب کنید',
    )
    url_title = models.CharField(max_length=300, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند محصول'
        verbose_name_plural = 'برند محصولات'


@register_snippet
class ProductColor(models.Model):
    ''' Product Color '''
    color_title = models.CharField(max_length=30, verbose_name='نام رنگ', db_index=True)
    color = ColorField()
    pquantity = models.IntegerField(verbose_name='تعداد رنگ بندی :')
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='مجموعه برای رنگ بندی انتخاب کنید',
    )

    

    panels = [
        FieldPanel('color_title'),
        NativeColorPanel('color'),
        FieldPanel('pquantity'),
        FieldPanel('collection'),
        ]

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'رنگ بندی'
        verbose_name_plural = 'رنگ بندی محصولات'


class ProductIndex(RoutablePageMixin, Page):
    ''' PRODUCT INDEX PAGE '''
    intro = RichTextField(blank=True, verbose_name='نام صفحه محصولات سایت')
    objects = ProductPageManager()
    max_count = 1
    subpage_types = ['product.InventoryItem']
    parent_page_types = ['index.Index']
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    class Meta:
        verbose_name = 'صفحه محصولات'


@register_snippet
class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # For percentage discount, use max_digits=5, decimal_places=2
    start_date = models.DateField()
    end_date = models.DateField()

    products = models.ManyToManyField('InventoryItem', related_name='offers')

    def __str__(self):
        return self.name



@register_snippet
class InventoryItem(RoutablePageMixin, Page):
    ''' Inventory => &&& <= Products '''
    product_title = models.CharField(max_length=300, verbose_name='نام و مدل محصول', null=True, blank=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    comments = models.ManyToManyField(Comment, blank=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='یک مجموعه برای محصول انتخاب کنید',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='تصویر / تصاویر محصول',
        help_text='تصویر/تصاویر محصول را اضافه کنید',
    )
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول', null=False)
    date = models.DateTimeField("Post date", default=timezone.now)
    brand = models.OneToOneField(ProductBrand, on_delete=models.PROTECT, verbose_name='برند', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت', blank=False, null=False)
    short_description = models.CharField(max_length=360, db_index=True, null=True, blank=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True, null=True, blank=True)
    colors = models.OneToOneField(ProductColor, null=True, blank=True, verbose_name='رنگ بندی محصول:', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال', blank=False, null=False)
    is_available = models.BooleanField(default=True, verbose_name='موجودی / عدم موجودی', blank=False, null=False)
    total_visits = models.IntegerField(verbose_name='تعداد کل بازدید', default=0)
    subpage_types = []
    parent_page_types = ['product.ProductIndex']
    content_panels = Page.content_panels + [
        FieldPanel('product_title'),
        FieldPanel('brand'),
        FieldPanel('price'),
        FieldPanel('image'),
        FieldPanel('quantity'),
        FieldPanel('short_description'),
        FieldPanel('description'),
        FieldPanel('colors'),
        FieldPanel('is_active'),
        FieldPanel('collection'),
    ]

    def apply_discount(self):
        current_date = timezone.now().date()
        offers = self.offers.filter(start_date__lte=current_date, end_date__gte=current_date)

        if offers.exists():
            # Assuming a product can have multiple offers, choose the highest discount
            max_discount = max(offers.values_list('discount', flat=True))
            if max_discount > 0:
                if max_discount <= 1:
                    # Percentage discount
                    discount_amount = self.price * Decimal(max_discount)
                else:
                    # Fixed amount discount
                    discount_amount = Decimal(max_discount)

                final_price = self.price - discount_amount
                return final_price

            return self.price
    
    @property
    def total_visits(self):
        return self.productvisit_set.aggregate(total=models.Sum('visit'))['total'] or 0

    @staticmethod
    def top_sales_products(limit=5):
        return Product.objects.annotate(total_sales=models.Sum('sales__quantity')).order_by('-total_sales')[:limit]

    top_sales_products.short_description = 'پر فروش ترین محصولات'

    def __str__(self):
        return f"{self.product_title} - {self.quantity} in stock"

    def restock(self, quantity):
        self.quantity += quantity
        if self.quantity > 0:
            self.is_available = True
        self.save()

    restock.short_description = 'شارژ محصول'

    def sell(self, quantity):
        if self.is_available and self.quantity >= quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.is_available = False
            self.save()
            return True
        else:
            return False

    sell.short_description = 'فروش محصول'

    def get_colors(self):
        return ", ".join([color.name for color in self.colors.all()]) if self.colors.exists() else "محصول بدون رنگ بندی است"

    get_colors.short_description = 'رنگ بندی محصول'

    def get_product_quantity(self):
        return self.quantity

    def get_product_total_sales(self):
        return self.invoiceitem_set.aggregate(Sum('quantity'))['quantity__sum'] or 0

    def get_product_total_visits(self):
        return self.productvisit_set.count()

    def get_product_sales_by_date(self, start_date, end_date):
        sales = self.invoiceitem_set.filter(
            invoice__date__range=[start_date, end_date]
        ).values_list('quantity', flat=True)
        return list(sales)

    def get_product_sales_mean(self, start_date, end_date):
        sales = self.invoiceitem_set.filter(
            invoice__date__range=[start_date, end_date]
        ).values_list('quantity', flat=True)
        mean_sales = pd.Series(sales).mean()
        return mean_sales

    def get_product_sales_variance(self, start_date, end_date):
        sales = self.invoiceitem_set.filter(
            invoice__date__range=[start_date, end_date]
        ).values_list('quantity', flat=True)
        variance_sales = pd.Series(sales).var()
        return variance_sales

    def get_product_sales_std(self, start_date, end_date):
        sales = self.invoiceitem_set.filter(
            invoice__date__range=[start_date, end_date]
        ).values_list('quantity', flat=True)
        std_sales = pd.Series(sales).std()
        return std_sales

    def get_product_sales_quartiles(self, start_date, end_date):
        sales = self.invoiceitem_set.filter(
            invoice__date__range=[start_date, end_date]
        ).values_list('quantity', flat=True)
        quartiles = pd.Series(sales).quantile([0.25, 0.5, 0.75])
        return quartiles.tolist()

    def get_product_balance_distribution(self):
        try:
            total_inventory = self.inventoryitem_set.aggregate(Sum('quantity'))['quantity__sum']
            balance_distribution = {}
            for item in self.inventoryitem_set.all():
                balance_distribution[item.product.name] = item.quantity / total_inventory
            return balance_distribution
        except InventoryItem.DoesNotExist:
            return {}

    def jpub(self):
        return jConvert(self.date)

    jpub.short_description = 'زمان انتشار'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        loaded_product = Product.objects.live().order_by('-first_published_at')
        context['products'] = loaded_product if loaded_product is not None else 0
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs)
        )

    def save(self, *args, **kwargs):
        if not self.is_available:
            self.is_available = False
        super().save(*args, **kwargs)

    save.short_description = 'ذخیره محصول'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


@register_snippet
class ProductVisit(models.Model):
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, verbose_name='محصول')
    ip_address = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,)
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='زمانبندی بازدید')

    class Meta:
        verbose_name = 'بازدید کالا'
        verbose_name_plural = 'بازدیدهای محصولات'

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        super().save(*args, **kwargs)

    save.short_description = 'ذخیره بازدید محصول'


@register_snippet
class PopularProduct(models.Model):
    product_visited = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    total_visit = models.IntegerField(verbose_name='تعداد کل بازدید', default=0)

    class Meta:
        verbose_name = 'محصول محبوب'
        verbose_name_plural = 'محصولات محبوب'

    @classmethod
    def update_popularity(cls):
        popular_products = cls.objects.all().order_by('-total_visit')[:5]
        # بروزرسانی لیست محصولات محبوب

    def save(self, *args, **kwargs):
        self.total_visit = self.product_visited.productvisit_set.count()
        super().save(*args, **kwargs)

    save.short_description = 'مجموع بازدیدهای محصول'


@register_snippet
class Inventory(models.Model):
    products = models.ForeignKey(InventoryItem, blank=True, null=True, on_delete=SET_NULL)

    def sell_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            return product.sell(quantity)
        except InventoryItem.DoesNotExist:
            return False

    def restock_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            product.restock(quantity)
            return True
        except InventoryItem.DoesNotExist:
            return False

    class Meta:
        verbose_name = 'انبار کالا'
        verbose_name_plural = 'انبار کالا'


@register_snippet
class CartItem(models.Model):
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مجموع')
    
    class Meta:
        verbose_name = 'آیتم سبد خرید'
        verbose_name_plural = 'آیتم‌های سبد خرید'



class Invoice(models.Model):
    date = models.DateField(default=timezone.now)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    product = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)


class ExportManager:
    def export_to_pdf(self):
        products = InventoryItem.objects.all()
        data = {'InventoryItem Name': [], 'Total Sales': [], 'Total Visits': []}
        for product in products:
            data['InventoryItem Name'].append(product.name)
            data['Total Sales'].append(product.get_product_total_sales())
            data['Total Visits'].append(product.get_product_total_visits())

        df = pd.DataFrame(data)
        output_path = 'product_sales.pdf'
        df.to_pdf(output_path)

        return output_path

    def export_to_excel(self):
        products = ProInventoryItemduct.objects.all()
        data = {'InventoryItem Name': [], 'Total Sales': [], 'Total Visits': []}
        for product in products:
            data['InventoryItem Name'].append(product.name)
            data['Total Sales'].append(product.get_product_total_sales())
            data['Total Visits'].append(product.get_product_total_visits())

        df = pd.DataFrame(data)
        output_path = 'product_sales.xlsx'
        df.to_excel(output_path)

        return output_path