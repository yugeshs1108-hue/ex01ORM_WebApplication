# Ex01 Django ORM Web Application
## Date: 30/11/2025

## AIM
To develop a Django application to store and retrieve data from a product Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 2 products

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import Product,ProductAdmin
# Register your models here.
admin.site.register(Product,ProductAdmin) 

```
## OUTPUT
<img width="1915" height="828" alt="Screenshot 2025-11-30 145938" src="https://github.com/user-attachments/assets/419e5ba9-93f8-43bb-b476-e2cd11b31ef7" />


## RESULT
Thus the program for creating product database using ORM hass been executed successfully
