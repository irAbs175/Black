from inventory.models import (Products, Materials)
from import_export import resources
 

class ProductsResource(resources.ModelResource):
    class Meta:
        model = Products


class MaterialsResource(resources.ModelResource):
    class Meta:
        model = Materials