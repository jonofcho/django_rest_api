from pricerules import services
import json
from pprint import pprint

# create product choices
products_list = services.get_products()
PRODUCT_CHOICES = ()

for product in products_list.get('products'):
    PRODUCT_CHOICES += (product.get('id') , (product.get('title'))),
# pprint(PRODUCT_CHOICES)

VARIANT_CHOICES = ()
for product in products_list.get('products'):
    for variant in product.get('variants'):
        VARIANT_CHOICES += (variant.get('id'), (variant.get('sku'))),

TARGET_TYPE_CHOICES = (
    ("line_item", ("Line Item")),
    ("shipping_line", ("Shipping Line"))
)

TARGET_SELECTION_CHOICES = (
    ('all', ("all")),
    ('entitled', ("entitled"))
)

ALLOCATION_METHOD_CHOICES = (
    ('across', ("across")),
    ('each', ("each"))
)
VALUE_TYPE_CHOICES = (
    ('fixed_amount', ("fixed_amount")),
    ('percentage', ("percentage"))
)

ONCE_PER_CUSTOMER_CHOICES = (
    (True, ("True")),
    (False, ("False"))
)

CUSTOMER_SELECTION_CHOICES = (
    ('all', ("all")),
    ('prerequisite', ("prerequisite"))
)
