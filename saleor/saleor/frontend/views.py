from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import requests,json
from django import forms
from django.core.mail import send_mail
from .forms import ContactForm
from django import forms
from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, "frontend/index.html", {})


def about(request):
    return TemplateResponse(request, "frontend/about.html", {})


def campus(request):
    url = "https://pos.globalfoodsoft.com/pos/menu"
    headers = {
        'authorization': "1yb9CBnkH4bv58xMo",
        'accept': "application/json",
        'glf-api-version': "2"
    }
    response = requests.request("GET", url, headers=headers)
    return TemplateResponse(request, "frontend/campus.html", {})


def contact(request):
    form = ContactForm()
    return TemplateResponse(request, "frontend/contact.html", {'form': form})


def emailsent(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']
            sendername = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = ['info@horizondesigns.ca', 'ismailmare@gmail.com']
            #send_mail(subject, message, sender, recipients)
            return TemplateResponse(request, "frontend/emailsent.html", {})

    else:
        form = ContactForm()
        return TemplateResponse(request, "frontend/contact.html", {'form': form})
