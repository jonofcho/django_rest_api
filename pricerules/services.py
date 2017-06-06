import requests
import json
from .objects import *

pr_url = "https://eac627f1da25d65f926d6fdd74e287a0:c8c7213be9e11fb402507e41e8be153b@cube-and-dice.myshopify.com/admin/price_rules.json"
pr_update_url = "https://eac627f1da25d65f926d6fdd74e287a0:c8c7213be9e11fb402507e41e8be153b@cube-and-dice.myshopify.com/admin/price_rules/%s.json"
jsonheaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
## RETREIVE ALL PRICE RULES FROM SHOPIFY
def get_price_rules():
    url = pr_url
    # params = {'id': id, 'value': value}
    r = requests.get(url)
    price_rules = r.json()
    # r = json.loads(price_rules)
    # books_list = {'books':books['results']}
    return price_rules

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

def post_update_price_rule(price_rule , price_rule_id):
    url = pr_update_url % (price_rule_id)
    r = requests.put(url , data=price_rule , headers=jsonheaders)

def post_delete_price_rule(price_rule_id):
    url = pr_update_url % (price_rule_id)
    r = requests.delete(url, headers=jsonheaders)
