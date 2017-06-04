import requests
import json
import .objects
def get_price_rules():
    url = 'add here'
    # params = {'id': id, 'value': value}
    r = requests.get(url)
    price_rules = r.json()
    # r = json.loads(price_rules)
    # books_list = {'books':books['results']}
    return price_rules

def get_discounts(price_rule_id):
    url = "add here" % (price_rule_id)
    print(url)
    r = requests.get(url)
    discount_codes = r.json()

    return discount_codes


def post_price_rule(price_rule):
    url = 'add here'
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
