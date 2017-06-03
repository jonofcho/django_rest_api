from django.shortcuts import render
from discounts import services
# Create your views here.

def index(request):
    price_rule_list = services.get_price_rules()
    context = {
        'price_rule_list' : price_rule_list
    }
    return render(request, 'discounts/index.html', context)

def detail(request , price_rule_id):
    discounts_list = services.get_discounts(price_rule_id)
    print(discounts_list)
    context = {
        'discounts_list' : discounts_list
    }
    return render(request, 'discounts/detail.html', context)
