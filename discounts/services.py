import requests
import json
from .objects import *
access = "ENTER HERE"https://eac627f1da25d65f926d6fdd74e287a0:c8c7213be9e11fb402507e41e8be153b@""
pr_url = "%scube-and-dice.myshopify.com/admin/price_rules.json" % (access)
dc_url = "%scube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json" % (access)
pr_update_url = "%scube-and-dice.myshopify.com/admin/price_rules/%s.json" % (access)
dc_new_url = "%scube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json" % (access)
jsonheaders = {'Content-type': 'application/json', 'Accept': 'text/plain'} % (access)

def get_price_rules():
    url = pr_url
    # params = {'id': id, 'value': value}
    r = requests.get(url)
    price_rules = r.json()
    # r = json.loads(price_rules)
    # books_list = {'books':books['results']}
    return price_rules

def get_discounts(price_rule_id):
    url = dc_url % (price_rule_id)
    r = requests.get(url)
    discount_codes = r.json()

    return discount_codes


def post_price_rule(price_rule):
    url = pr_url
    r = requests.post(url , data=price_rule, headers=jsonheaders)
    # response = r.text
    # print(r)
    # print(price_rule)
    print('post has been made')
    print(r.text)

def post_update_price_rule(price_rule , price_rule_id):
    url = pr_update_url % (price_rule_id)
    r = requests.put(url , data=price_rule , headers=jsonheaders)
    print('update has been made')
    print(r.text)
def post_delete_price_rule(price_rule_id):
    url = pr_update_url % (price_rule_id)
    r = requests.delete(url, headers=jsonheaders)

def create_price_rule(post):
    price_rule = PriceRule(post)
    c = {
        'price_rule' : price_rule
    }
    return json.dumps(c, default=lambda o: o.__dict__,sort_keys=True, indent=4)

def update_price_rule(update):
    price_rule = PriceRule(update)
    c = {
        'price_rule' : price_rule
    }
    return json.dumps(c, default=lambda o: o.__dict__,sort_keys=True, indent=4)

def create_discount_code(post):
    print(post)
    discount_code = Discount(post)

    c = {
        'discount_code' : discount_code
    }
    return json.dumps(c , default=lambda o: o.__dict__, sort_keys=True, indent=4)

def post_discount_code(price_rule_id , discount_code):
    url = dc_new_url % (price_rule_id)
    r = requests.post(url , data=discount_code, headers=jsonheaders)
