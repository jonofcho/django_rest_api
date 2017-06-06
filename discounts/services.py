import requests
import json
from .objects import *

dc_url = "https://eac627f1da25d65f926d6fdd74e287a0:c8c7213be9e11fb402507e41e8be153b@cube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json"
dc_new_url = "https://eac627f1da25d65f926d6fdd74e287a0:c8c7213be9e11fb402507e41e8be153b@cube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json"
jsonheaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def get_discounts(price_rule_id):
    url = dc_url % (price_rule_id)
    r = requests.get(url)
    discount_codes = r.json()

    return discount_codes

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
