from django.contrib import admin
from .models import Product,Contact
# name : Ecommerce
# pass : admin@123

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)