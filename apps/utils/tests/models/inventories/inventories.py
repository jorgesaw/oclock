"""Inventories models utilities for testing."""

# models
from apps.inventories.models import (
    Category, 
    Product, 
    SubCategory
)

CATEGORY_NAME = 'CategYÑ099.h¡8y+)¿99hsw'
PRODUCT_NAME = 'Product}{88-_.,+}{lñ'
SUBCATEGORY_NAME = 'Subc576ñ.{'

def create_category(name=CATEGORY_NAME, active=True):
    return Category.objects.create(
        name=name, 
        active=active
    )


def create_subcategory(name=SUBCATEGORY_NAME, 
    active=True, category=None):
    
    if not category:
        category = Category.objects.create(name=CATEGORY_NAME)
    return SubCategory.objects.create(
        name=name,
        active=active, 
        category=category
    )


def create_product(**kwargs):
    code = kwargs.get('code', '1234567890')
    barcode = kwargs.get('barcode', 'BARCODE1234567890')
    name = kwargs.get('name', PRODUCT_NAME)
    desc = kwargs.get('desc', PRODUCT_NAME)
    price =kwargs.get('price', 13.13)
    stock = kwargs.get('stock', 10)
    stock_min = kwargs.get('stock_min', 0)
    stock_max = kwargs.get('stock_max', 10000)
    picture = kwargs.get('picture', None)
    active = kwargs.get('active', True)
    subcategory = kwargs.get('subcategory')

    return Product.objects.create(
        code=code, barcode=barcode, name=name,
        desc=desc, price=price, stock=stock, 
        stock_min=stock_min, stock_max=stock_max, 
        picture=picture, active=active, 
        subcategory=subcategory
    )
