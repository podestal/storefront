from django_filters.rest_framework import FilterSet
from .models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            #  this is filtering the price which gives a range 
            'unit_price': ['gt', 'lt']
        }