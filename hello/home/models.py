from django.db import models


#makemigrations - create changes and store in a file
#migrate-apply the pending changes created by make migrations#
class Contact(models.Model):
       name= models.CharField(max_length=122)
       email= models.CharField( max_length=122)
       phone= models.CharField(max_length=12)
       desc= models.TextField()
       date= models.DateField()
       from django.db import models

from django.db import models

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.TextField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return f'{self.customer_name} - {self.date_created}'


def __str__(self):
        return self.name

from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
from django.db import models

class CartItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - ${self.price:.2f}'








