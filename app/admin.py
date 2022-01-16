from django.contrib import admin
from . import models

admin.site.register(models.Service)
admin.site.register(models.Availability)
admin.site.register(models.Order)
