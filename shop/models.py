from django.db import models
from django.utils import timezone


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,default='')
    phone = models.IntegerField(max_length=12,default='')
    desc = models.TextField(max_length=400,default='')
    DateTime = models.DateTimeField(default =timezone.now)

    def __str__(self):
        return self.name