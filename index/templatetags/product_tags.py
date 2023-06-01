from django import template
from product.models import InventoryItem


register = template.Library()

@register.inclusion_tag('index/index.html', takes_context=True)
def product(context):
    return {
        'products': InventoryItem.objects.all(),
        'request': context['request'],
    }