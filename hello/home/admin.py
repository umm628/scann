from django.contrib import admin
from  home.models import Contact

# Register your models here.
admin.site.register(Contact)

from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'items', 'total_price', )

admin.site.register(Order, OrderAdmin)

