from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):

    return HttpResponseRedirect(reverse('pricerules:index'))
