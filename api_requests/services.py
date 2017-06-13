import requests
import json
from passwords import KEYPASS
from pprint import pprint
pr_url = KEYPASS + "@cube-and-dice.myshopify.com/admin/price_rules/%s.json"
dc_url = KEYPASS + "@cube-and-dice.myshopify.com/admin/price_rules/%s/discount_codes.json"

def get_pr_data(price_rule_id):
    url = pr_url % (price_rule_id)
    r = requests.get(url)
    result = r.json()
    return result

def get_dc_data(price_rule_id):
    url = dc_url % (price_rule_id)
    r = requests.get(url)
    result = r.json()
    return result
