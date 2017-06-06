from django.shortcuts import render
from discounts import services
from .forms import *
# Create your views here.
def index(request):
    price_rule_list = services.get_price_rules()
    context = {
        'price_rule_list' : price_rule_list
    }
    return render(request, 'discounts/index.html', context)

def create(request):
    if request.method == "POST":
        form = PriceRuleForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            new_price_rule = services.create_price_rule(form.cleaned_data)
            services.post_price_rule(new_price_rule)
            return render(request, 'discounts/index.html')
    else:
        form = PriceRuleForm()
    return render(request , 'discounts/new_pr.html', { 'form' : form })

def update(request , price_rule_id):
    if request.method == "POST":
        form = PriceRuleUpdateForm(request.POST)
        if form.is_valid():
            print('form is valid')
            updated_price_rule = services.update_price_rule(form.cleaned_data)
            services.post_update_price_rule(updated_price_rule , price_rule_id)
            return render(request , 'discounts/index.html')
        else:
            print('form is invalid')
    else:
        print('request is not put')
        form = PriceRuleUpdateForm()
    return render(request , 'discounts/update_pr.html', { 'form': form })

def delete(request , price_rule_id):
    # ASK USER TO PROVIDE LOG IN CREDENTIALS
    print(price_rule_id)
    services.post_delete_price_rule(price_rule_id)
    return render(request , 'discounts/delete_pr.html')
