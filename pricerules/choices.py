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
