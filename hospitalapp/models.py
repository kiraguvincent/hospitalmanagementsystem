from django.db import models

# Create your models here.
class users(models.Model):
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

class Member(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Message(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField()
        subject = models.CharField(max_length=200)
        message = models.TextField()
        def __str__(self):
            return self.name
class Appointment(models.Model):
    YourName = models.CharField(max_length=200)
    YourEmail = models.EmailField()
    YourPhone= models.IntegerField(max_length=200)
    AppointmentDate = models.DateField()
    Department = models.CharField(max_length=200)
    Doctor = models.CharField(max_length=200)
    Message = models.TextField()


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)