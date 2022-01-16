from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('agendamento/', views.agendar, name='agendamento'),
    path('new-home/', views.newHome, name='newHome'),
]