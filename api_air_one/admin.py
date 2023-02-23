from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.City)
admin.site.register(models.Plane)
admin.site.register(models.Route)
