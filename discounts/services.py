import requests
import json
from .objects import *
from passwords import KEYPASS

dc_url = KEYPASS + "@cube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json"
dc_new_url = KEYPASS +"@cube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json"
jsonheaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def get_discounts(price_rule_id):
    url = dc_url % (price_rule_id)
    r = requests.get(url)
    discount_codes = r.json()

    return discount_codes

def create_discount_code(post):
    discount_code = Discount(post)
    c = {
        'discount_code' : discount_code
    }
    return json.dumps(c , default=lambda o: o.__dict__, sort_keys=True, indent=4)

def post_discount_code(price_rule_id , discount_code):
    url = dc_new_url % (price_rule_id)
    r = requests.post(url , data=discount_code, headers=jsonheaders)
    print(r.text)
