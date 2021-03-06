from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from pricerules import services
from .forms import *
from django.contrib.auth.decorators import login_required
import json

@login_required
# Create your views here.
def index(request):
    price_rule_list = services.get_price_rules()
    # print(price_rule_list)
    # print(json.dumps(price_rule_list, indent=4, sort_keys=True))
    context = {
        'price_rule_list' : price_rule_list
    }
    return render(request, 'pricerules/index.html', context)

def create(request):
    if request.method == "POST":
        form = PriceRuleForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            new_price_rule = services.create_price_rule(form.cleaned_data)
            print(new_price_rule)
            new_price_rule_id = services.post_price_rule(new_price_rule)
            return HttpResponseRedirect(reverse('discounts:detail' , args=(new_price_rule_id,)))
        else:
            print('didnt work')
    else:
        form = PriceRuleForm()

    return render(request , 'pricerules/create.html', {'form' : form})

def update(request , price_rule_id):
    if request.method == "POST":
        form = PriceRuleForm(request.POST)
        if form.is_valid():
            print('form is valid')
            updated_price_rule = services.update_price_rule(form.cleaned_data)
            services.post_update_price_rule(updated_price_rule , price_rule_id)
            return render(request , 'pricerules/index.html')
        else:
            print(form.cleaned_data)
            print('form is invalid')
    else:
        print('request is not put')
        price_rule = services.get_single_price_rule(price_rule_id)

        form = PriceRuleForm(price_rule.get('price_rule'))
    return render(request , 'pricerules/update.html', { 'form': form })

def delete(request , price_rule_id):
    # ASK USER TO PROVIDE LOG IN CREDENTIALS
    print(price_rule_id)
    services.post_delete_price_rule(price_rule_id)
    return HttpResponseRedirect(reverse('pricerules:index'))
