from django.shortcuts import render
from discounts import services
from .forms import PriceRuleForm , PriceRuleUpdateForm
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

def new_pr(request):
    if request.method == "POST":
        form = PriceRuleForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            new_price_rule = services.create_price_rule(form.cleaned_data)
            services.post_price_rule(new_price_rule)
            return render(request, 'discounts/index.html')
    else:
        form = PriceRuleForm()
    return render(request , 'discounts/new_pr.html', { 'form' : form })

def update_pr(request , price_rule_id):
    if request.method == "post":
        form = PriceRuleUpdateForm(request.PUT)
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

def delete_pr(request , price_rule_id):
    context = {
        'price_rule_id' : price_rule_id
    }
    return render(request , 'discounts/delete_pr.html', context)

def new_dc(request):

    return render(request, 'discounts/new_dc.html')
