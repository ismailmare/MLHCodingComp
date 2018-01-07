from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import requests,json

def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def campus(request):
    url = "https://pos.globalfoodsoft.com/pos/menu"

    headers = {
        'authorization': "1yb9CBnkH4bv58xMo",
        'accept': "application/json",
        'glf-api-version': "2"
    }

    response = requests.request("GET", url, headers=headers)



    return render(request, "campus.html", {})