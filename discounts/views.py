from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from discounts import services
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def detail(request , price_rule_id):
    discounts_list = services.get_discounts(price_rule_id)
    print(discounts_list)
    context = {
        'price_rule_id' : price_rule_id ,
        'discounts_list' : discounts_list
    }
    return render(request, 'discounts/detail.html', context)

def create(request, price_rule_id):
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            new_discount_code = services.create_discount_code(form.cleaned_data)
            services.post_discount_code(new_discount_code, price_rule_id)
            return HttpResponseRedirect(reverse('discounts:detail' , args=(price_rule_id,)))
    else:
        form = DiscountForm()
    return render(request , 'discounts/create.html', { 'form' : form })
