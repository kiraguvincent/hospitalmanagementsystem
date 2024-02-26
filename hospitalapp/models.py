from django.db import models

# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    yearofbirth = models.IntegerField(null=True)

    def __str__(self):
        return self.fullname

class Product(models.Model):
        Product_name = models.CharField(max_length=200)
        Product_price = models.CharField(max_length=100)
        Product_quantity = models.IntegerField()

        def __str__(self):
            return self.Product_name
