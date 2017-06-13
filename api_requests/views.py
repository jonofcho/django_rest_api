from django.shortcuts import render
from rest_framework import viewsets
from pprint import pprint
from api_requests import services
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .objects import NewJsonObject
from django.core import serializers
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def get_pr(request , price_rule_id):
     print(price_rule_id)
     pr_data = services.get_pr_data(price_rule_id)
     dc_data = services.get_dc_data(price_rule_id)
     final_data = NewJsonObject(pr_data , dc_data)
     serialized_obj = json.dumps(final_data, default=lambda o: o.__dict__)
     print(serialized_obj)
     return Response(serialized_obj)
