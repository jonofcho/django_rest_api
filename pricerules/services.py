import requests
import json
from .objects import *
from pprint import pprint
import datetime
from passwords import KEYPASS

all_products = KEYPASS +"@cube-and-dice.myshopify.com/admin/products.json?fields=variants,id,sku,title"
pr_url = KEYPASS +"@cube-and-dice.myshopify.com/admin/price_rules.json"
pr_update_url = KEYPASS +"@cube-and-dice.myshopify.com/admin/price_rules/%s.json"
jsonheaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# GET ATLL SHOPIFY PRODUCTDS
def get_products():
    url = all_products
    r = requests.get(url)
    products = r.json()
    return products
## RETREIVE ALL PRICE RULES FROM SHOPIFY
def get_price_rules():
    url = pr_url
    # params = {'id': id, 'value': value}
    r = requests.get(url)
    price_rules = r.json()
    # r = json.loads(price_rules)
    # books_list = {'books':books['results']}
    return price_rules

def get_single_price_rule(price_rule_id):
    url = pr_update_url % (price_rule_id)
    r = requests.get(url)
    price_rule = r.json()
    return price_rule
# OBJECTIFY/JSONIFY ALL FORM DATA
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

# SEND DATA TO SHOPIFY
def post_price_rule(price_rule):
    url = pr_url
    r = requests.post(url , data=price_rule, headers=jsonheaders)
    print(r.text)
    new_price_rule_id = r.json().get('price_rule').get('id')
    return new_price_rule_id

def post_update_price_rule(price_rule , price_rule_id):
    url = pr_update_url % (price_rule_id)
    r = requests.put(url , data=price_rule , headers=jsonheaders)

def post_delete_price_rule(price_rule_id):
    url = pr_update_url % (price_rule_id)
    r = requests.delete(url, headers=jsonheaders)
