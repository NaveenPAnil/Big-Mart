from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    CategoryName = models.CharField(max_length=50,blank=True,null=True)
    Description = models.CharField(max_length=500,blank=True,null=True)
    Image = models.ImageField(upload_to="categories",blank=True,null=True)

class ProductDB(models.Model):
    CategoryName = models.CharField(max_length=50,blank=True,null=True)
    ProductName = models.CharField(max_length=50,blank=True,null=True)
    Quantity = models.CharField(max_length=50,blank=True,null=True)
    Price = models.IntegerField(blank=True,null=True)
    ProductImage = models.ImageField(upload_to="products",blank=True,null=True)