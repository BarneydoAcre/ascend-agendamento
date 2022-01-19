from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *

import json

def home(request):
    data = {}
    data['item'] = Service.objects.all()
    data['aval'] = Availability.objects.all().order_by('-id')
    data['form_order'] = CreateOrder()

    db = CreateOrder()

    return render(request, 'app/home.html', data)

@login_required
def agendar(request):
    if request.method == "POST":
        form = CreateOrder(request.POST)
        if form.is_valid():
            form.save()
            
            busy = Availability.objects.get(id=request.POST['availability'])
            busy.busy = True
            busy.save()
            messages.add_message(request, messages.INFO, 'Cadastro Realizado!')
            return HttpResponseRedirect('/')
        else:
            form = CreateOrder()

            busy = Availability.objects.get(id=request.POST['availability'])
            busy.busy = False
            busy.save()
    messages.add_message(request, messages.INFO, 'Agendamento mal sucedido!')
    return HttpResponseRedirect('/')

@login_required
def meusAgendamentos(request):
    data = {}
    data['item'] = Service.objects.all()
    data['order'] = Order.objects.filter(user=request.session['_auth_user_id'])
    data['avail'] = Availability.objects.all()

    return render(request, 'app/meusAgendamentos.html', data)

@login_required
def cancelarAgendamento(request):
    order = Order.objects.filter(user=request.session['_auth_user_id'], availability=request.POST['availability'])
    print(order)
    order.delete()

    availability = Availability.objects.get(id=request.POST['availability'])
    availability.busy = False
    availability.save()

    return HttpResponseRedirect('/meus-agendamentos/')