from django.db import models

# Create your models here.
class RegistrationDB(models.Model):
    Username = models.CharField(max_length=50,blank=True,null=True)
    Mail = models.EmailField(max_length=50,blank=True,null=True)
    Password = models.CharField(max_length=50,blank=True,null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    Image = models.ImageField(upload_to="userimg",blank=True,null=True)

class CartDB(models.Model):
    Username = models.CharField(max_length=50,blank=True,null=True)
    ProductName = models.CharField(max_length=50,blank=True,null=True)
    Quantity = models.CharField(max_length=50,blank=True,null=True)
    TotalPrice = models.IntegerField(max_length=50,blank=True,null=True)

class CheckoutDB(models.Model):
    Name = models.CharField(max_length=50,blank=True,null=True)
    Country = models.CharField(max_length=50,blank=True,null=True)
    State = models.CharField(max_length=50,blank=True,null=True)
    Address = models.CharField(max_length=500,blank=True,null=True)
    Email = models.EmailField(max_length=500,blank=True,null=True)
    Town = models.CharField(max_length=500,blank=True,null=True)
    Phone = models.IntegerField(max_length=500,blank=True,null=True)
