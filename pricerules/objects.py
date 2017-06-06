class PriceRule(object):
    print(object)
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
    entitled_product_ids =  []
    # entitled_variant_ids =  []
    # entitled_collection_ids =  []
    # entitled_country_ids =  []
    starts_at =  '2017-06-04T02 = 33 = 48Z'

    def __init__(self , post):
        self.title = post['title']
        self.target_type = post['target_type']
        self.target_selection = post['target_selection']
        self.allocation_method =  post['allocation_method']
        self.value_type =  post['value_type']
        self.value =  post['value']
        self.once_per_customer = post['once_per_customer']
        self.usage_limit = post['usage_limit']
        self.customer_selection = post['customer_selection']
        self.starts_at =  '2017-06-06T02:33:48Z'
