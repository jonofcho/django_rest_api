import requests
import json

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


def get_price_rules():
    url = 'https://cc56bd88237c966d8b9c0535309ff6c0:8ffa8234118f87d0bd88cf40e6ea1c0a@cube-and-dice.myshopify.com/admin/price_rules.json'
    # params = {'id': id, 'value': value}
    r = requests.get(url)
    price_rules = r.json()
    # r = json.loads(price_rules)
    # books_list = {'books':books['results']}
    return price_rules

def get_discounts(price_rule_id):
    url = "https://cc56bd88237c966d8b9c0535309ff6c0:8ffa8234118f87d0bd88cf40e6ea1c0a@cube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json" % (price_rule_id)
    print(url)
    r = requests.get(url)
    discount_codes = r.json()

    return discount_codes


def post_price_rule(price_rule):
    url = 'https://cc56bd88237c966d8b9c0535309ff6c0:8ffa8234118f87d0bd88cf40e6ea1c0a@cube-and-dice.myshopify.com/admin/price_rules.json'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url , data=price_rule, headers=headers)
    # response = r.text
    # print(r)
    # print(price_rule)
    print('post has been made')
    print(r.text)

def create_price_rule(post):
    price_rule = PriceRule(post)
    c = {
        'price_rule' : price_rule
    }
    return json.dumps(c, default=lambda o: o.__dict__,sort_keys=True, indent=4)
