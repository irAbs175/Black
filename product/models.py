from index.extensions.jalali_converter import jalali_converter as jConvert
from wagtail.models import Page, PageManager, ClusterableModel, Orderable
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail_color_panel.edit_handlers import NativeColorPanel
from modelcluster.contrib.taggit import ClusterTaggableManager
from user_accounts.models import user_accounts as User
from django.template.response import TemplateResponse
from wagtail.snippets.models import register_snippet
from wagtail_color_panel.fields import ColorField
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.db import models


class ProductPageManager(PageManager):
    pass


@register_snippet
class ProductBrand(models.Model):
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
    color_title = models.CharField(max_length=10)
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
    intro = RichTextField(blank=True, verbose_name='نام صفحه محصولات سایت')
    objects = ProductPageManager()
    max_count = 1
    subpage_types = ['product.Product']
    parent_page_types = ['index.Index']
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    class Meta:
        verbose_name = 'صفحه محصولات'


@register_snippet
class Product(RoutablePageMixin, Page):
    product_title = models.CharField(max_length=300, verbose_name='نام و مدل محصول', null=True, blank=True)
    author = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL,)
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
    date = models.DateTimeField("Post date", default=timezone.now)
    brand = models.OneToOneField(ProductBrand, on_delete=models.PROTECT, verbose_name='برند', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت', blank=False, null=False)
    short_description = models.CharField(max_length=360, db_index=True, null=True, blank=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True, null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول', null=False)
    colors = models.OneToOneField(ProductColor, null=True, blank=True, verbose_name='رنگ بندی محصول :', on_delete=models.PROTECT)
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        loaded_product = Product.objects.live().order_by('-first_published_at')
        context['products'] = loaded_product if loaded_product is not None else 0
        return context

    def server(self, request, *args, **kwargs):
        return render(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs)
        )

    @property
    def total_visits(self):
        return self.productvisit_set.aggregate(total=models.Sum('visit'))['total'] or 0

    # total_visits.short_description = 'مجموع بازدید های محصول'

    @staticmethod
    def top_sales_products(limit=5):
        return Product.objects.annotate(total_sales=models.Sum('sales__quantity')).order_by('-total_sales')[:limit]

    top_sales_products.short_description = 'پر فروش ترین محصولات'

    def jpub(self):
        return jConvert(self.date)

    jpub.short_description = 'زمان انتشار'

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

    def restock(self, quantity):
        self.quantity += quantity
        if self.quantity > 0:
            self.is_available = True
        self.save()

    restock.short_description = 'شارژ محصول'

    def get_colors(self):
        return ", ".join([color.name for color in self.colors.all()]) if self.colors.exists() else "محصول بدون رنگ بندی است"

    get_colors.short_description = 'رنگ بندی محصول'

    def save(self, *args, **kwargs):
        if not self.is_available:
            self.is_available = False
        super().save(*args, **kwargs)

    save.short_description = 'ذخیره محصول'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    
class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.OneToOneField(User, null=True, blank=True, verbose_name='کاربر', on_delete=models.SET_NULL)
    visit = models.IntegerField(verbose_name='بازدید محصول', null=True, blank=True)

    class Meta:
        verbose_name = 'بازدید کالا'
        verbose_name_plural = 'بازدیدهای محصولات'

    def save(self, *args, **kwargs):
        if not self.id:
            self.visit = self.product.productvisit_set.count() + 1
        super().save(*args, **kwargs)

    save.short_description = 'ذخیره بازدید محصول'    


class PopularProduct(models.Model):
    product_visited = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_visit = models.IntegerField(verbose_name='تعداد کل بازدید', default=0)

    class Meta:
        verbose_name = 'محصول محبوب'
        verbose_name_plural = 'محصولات محبوب'

    @classmethod
    def update_popularity(cls):
        popular_products = cls.objects.all().order_by('-total_visit')[:5]
        # Update popular product list

    def save(self, *args, **kwargs):
        self.total_visit = self.product_visited.productvisit_set.count()
        super().save(*args, **kwargs)

    save.short_description = 'مجموع بازدید های محصول'



class Inventory(models.Model):
    products = models.ForeignKey(Product, blank=True, null=True,on_delete=models.SET_NULL,)

    def sell_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            return product.sell(quantity)
        except Product.DoesNotExist:
            return False

    def restock_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            product.restock(quantity)
            return True
        except Product.DoesNotExist:
            return False

    class Meta:
        verbose_name = 'انبار کالا'
        verbose_name_plural = 'انبار کالا'