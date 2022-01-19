from random import choices
from django.db import models
from django.contrib.auth.models import User



class Service(models.Model):
    title = models.CharField('Titulo',max_length=50)
    desc =  models.CharField('Descrição', max_length=150, blank=True)
    image = models.FileField('Imagem', upload_to='app/static/public/service_images/', blank=True)
    price = models.FloatField('Preço')
    sold_off = models.BooleanField(u'Não vender?', default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name, verbose_name_plural = "Serviço", "Serviços"
        ordering = ('title',)

    def __str__(self):
        return self.title




class Availability(models.Model):
    daily_hour_choices = (
        (1, "06 as 07"),
        (2, "07 as 08"),
        (3, "08 as 09"),
        (4, "09 as 10"),
        (5, "10 as 11"),
        (6, "11 as 12"),
        (7, "12 as 13"),
        (8, "13 as 14"),
        (9, "14 as 15"),
        (10, "15 as 16"),
        (11, "16 as 17"),
        (12, "17 as 18"),
        (13, "18 as 19"),
        (14, "19 as 20"),
        (15, "20 as 21"),
        (16, "21 as 22"),
    )
    weekly_day_choices = (
        (1, "Domingo"),
        (2, "Segunda-Feira"),
        (3, "Terça-Feira"),
        (4, "Quarta-Feira"),
        (5, "Quinta-Feira"),
        (6, "Sexta-Feira"),
        (7, "Sábado"),
    )
    weekly_day = models.IntegerField('Dia da semana', choices=weekly_day_choices, blank=False)
    daily_hour = models.IntegerField('Horário do dia', choices=daily_hour_choices, blank=False)
    busy = models.BooleanField('Ocupado', default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name, verbose_name_plural = "Disponibilidade", "Disponibilidades"
        ordering = ("weekly_day","daily_hour")

    def __str__(self):
        title_return = str(self.get_weekly_day_display()) + ' | ' + str(self.get_daily_hour_display())
        return title_return
        

class Order(models.Model):
    user = models.ForeignKey('Person', verbose_name="Pessoa",on_delete=models.PROTECT)
    service = models.ForeignKey("Service", verbose_name="Serviço", on_delete=models.PROTECT)
    availability = models.ForeignKey(
        "Availability", 
        verbose_name="Disponibilidade",
        on_delete=models.PROTECT,
        limit_choices_to={'busy': False})
    telefone = models.CharField("Telefone", max_length=15, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name, verbose_name_plural = "Pedido", "Pedidos"

    def __str__(self):
        title_return = str(self.user) + ' | ' + str(self.service) + ' | ' + str(self.availability)
        return title_return

class Person(User):
    class Meta:
        proxy = True