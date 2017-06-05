import requests
import json
from .objects import PriceRule
pr_url = "@cube-and-dice.myshopify.com/admin/price_rules.json"
dc_url = "@cube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json"
pr_update_url = "@cube-and-dice.myshopify.com/admin/price_rules/%s.json"
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
    print(url)
    r = requests.get(url)
    discount_codes = r.json()

    return discount_codes


def post_price_rule(price_rule):
    url = pr_url
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url , data=price_rule, headers=headers)
    # response = r.text
    # print(r)
    # print(price_rule)
    print('post has been made')
    print(r.text)

def post_update_price_rule(price_rule , price_rule_id):
    url = pr__update_url % (price_rule_id)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.put(url , data=price_rule , headers=headers)
    print('update has been made')
    print(r.text)

def create_price_rule(post):
    price_rule = PriceRule(post)
    c = {
        'price_rule' : price_rule
    }
    return json.dumps(c, default=lambda o: o.__dict__,sort_keys=True, indent=4)

def update_price_rule(update):
    c = {
        'price_rule' : price_rule
    }
    return json.dumps(c, default=lambda o: o.__dict__,sort_keys=True, indent=4)
