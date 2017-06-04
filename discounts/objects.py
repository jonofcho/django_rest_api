class PriceRule(object):

    title = "string"
    target_type = "line_item"
    target_selection =  "all"
    allocation_method =  "across"
    value_type =  "fixed_amount"
    value =  "-0.15"
    once_per_customer = 'true'
    usage_limit = 100
    customer_selection = 'all'
    # prerequisite_subtotal_range =  'null'
    # prerequisite_shipping_price_range =  'null'
    # prerequisite_saved_search_ids =  []
    # entitled_product_ids =  []
    # entitled_variant_ids =  []
    # entitled_collection_ids =  []
    # entitled_country_ids =  []
    starts_at =  '2017-06-04T02 = 33 = 48Z'

    def __init__(self , post):
        self.title = post['title']
        self.target_type = 'line_item'
        self.target_selection = 'all'
        self.allocation_method =  "across"
        self.value_type =  "fixed_amount"
        self.value =  "-3"
        self.once_per_customer = 'true'
        self.usage_limit = 100
        self.customer_selection = 'all'
        self.starts_at =  '2017-06-04T02:33:48Z'


    def __str__(self):
        return self.title
