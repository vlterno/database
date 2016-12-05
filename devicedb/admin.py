from django.contrib import admin
from .models import Pc, Notebook, Smartphone, Product

admin.site.register(Pc)
admin.site.register(Notebook)
admin.site.register(Smartphone)
admin.site.register(Product)