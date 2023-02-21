
from django.conf import settings
from django.db import models
from mainapp.models import Product

# Create your models here.
class CartManager(models.Manager):
    @property
    def amount(self):
        return sum(item.quantity for item in self.all())

    @property
    def total_cost(self):
        return sum(item.product.price * item.quantity for item in self.all())

    def total_quantity(self):
        return sum(item.quantity for item in self.all())


    def has_items(self):
        return bool(len(self.all()))



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField(default = 0)
    add_datetime = models.DateTimeField(auto_now_add = True)

    objects = CartManager()






