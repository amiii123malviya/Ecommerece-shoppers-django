from django.db import models

# Create your models here.

class AddProduct(models.Model):
    Product_name=models.CharField(max_length=200)
    Product_descip=models.CharField(max_length=200)
    Product_price=models.IntegerField()
    Product_image=models.ImageField(upload_to='images/')

    class Meta:
        db_table="AddProduct"