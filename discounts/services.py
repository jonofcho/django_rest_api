import requests
import json
def get_price_rules():
    url = 'PUT IN HERE'
    # params = {'id': id, 'value': value}
    r = requests.get(url)
    price_rules = r.json()
    # r = json.loads(price_rules)
    # books_list = {'books':books['results']}
    return price_rules

def get_discounts(price_rule_id):
    url = "PUT IN HERE" % (price_rule_id)
    print(url)
    r = requests.get(url)
    discount_codes = r.json()

    return discount_codes
