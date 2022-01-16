from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Availability, Service
from .forms import *

import json

def home(request):
    data = {}
    data['item'] = Service.objects.all()
    data['aval'] = Availability.objects.all()
    data['form_order'] = CreateOrder()

    db = CreateOrder()

    return render(request, 'app/home.html', data)

def agendar(request):
    if request.method == "POST":
        form = CreateOrder(request.POST)
        if form.is_valid():
            form.save()
            
            busy = Availability.objects.get(id=1)
            busy.busy = True
            busy.save()
            messages.add_message(request, messages.INFO, 'Cadastro Realizado!')
            return HttpResponseRedirect('/')
        else:
            form = CreateOrder()

            busy = Availability.objects.get(id=1)
            busy.busy = False
            busy.save()
    messages.add_message(request, messages.INFO, 'Agendamento mal sucedido!')
    return HttpResponseRedirect('/')

def newHome(request):
    return render(request, 'app/newHome.html')
