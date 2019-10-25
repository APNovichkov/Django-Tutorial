from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=2)
    price = models.IntegerField(default=10)

    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

    def num_of_toppings():
        return toppings.count
