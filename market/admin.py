from django.contrib import admin

# Register your models here.
from .models import item,Carts

admin.site.register(item)
admin.site.register(Carts)