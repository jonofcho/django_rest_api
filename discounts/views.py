from django.shortcuts import render
from discounts import services
from .forms import PriceRuleForm
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

def new_dc(request):

    return render(request, 'discounts/new_dc.html')
