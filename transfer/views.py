from django.shortcuts import render
from django.http import HttpResponse

from .models import Employees

from .database import Database

import json
# Create your views here.

def index(request):
    Database.populatedb()

    try:
        member_list = Employees.objects.all()
    except Employees.DoesNotExist:
         raise Http404("Nothing in the database")
         return
    context = {
        'member_list': member_list,
    }
    return render(request, 'transfer_info/index.html', context)

def result(request):
    json_format: json
    json_format = Database.conv_to_json()
    json_format = str(json_format)
    return HttpResponse(json_format)