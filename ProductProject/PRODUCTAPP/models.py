from django.db import models
from django.contrib import admin
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50,help_text="Enter Product Name")
    price=models.IntegerField(help_text="Enter Product Price")
    mfg_date=models.DateField(help_text="Manufacture Date")
    product_code=models.CharField(help_text="Enter Product Code")
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price','mfg_date','product_code']
