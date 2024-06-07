from django.db import models

# Create your models here.

class AddProduct(models.Model):
    Product_name=models.CharField(max_length=200)
    Product_descip=models.CharField(max_length=200)
    Product_price=models.IntegerField()
    Product_image=models.ImageField(upload_to='images/')

    class Meta:
        db_table="AddProduct"
class Details(models.Model):
        amount = models.IntegerField()
        order_id = models.CharField(max_length=1000 )
        razorpay_payment_id = models.CharField(max_length=1000 ,blank=True)
        paid = models.BooleanField(default=False)
        def __str__(self):
            return self.name
class Register(models.Model):
    Name=models.CharField(max_length=300)
    Email=models.EmailField()
    Contact=models.IntegerField()
    City=models.CharField(max_length=250)
    Password=models.CharField(max_length=300)


    class Meta:
        db_table='Register'
        verbose_name_plural='Register'
    def __str__(self):
        return self.Name