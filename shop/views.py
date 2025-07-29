from django.shortcuts import render
from math import ceil
from django.http import HttpResponse
from .models import Product,Contact
from django.contrib import messages

def index(request):
    # products  = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # allProds = [
    #             [products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides],
    #             ]
    allProds = []
    catprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prods = Product.objects.filter(category = cat)
        n = len(prods)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prods,range(1,nSlides),nSlides])


    # params = {'nslides' : nslides, 'range' : range(nslides), 'product' : products}
    params = {'allProds' : allProds}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        desc = request.POST.get('desc' , '')
        # print(name,email,phone,desc)
        contact = Contact(name = name,email=email, phone = phone, desc = desc )
        contact.save()
        messages.success(request, "Your message has been send!,Thanks for contact us!")
    return render(request , 'shop/contact.html')

def tracker(request):
    return render(request , 'shop/tracker.html')

def search(request):
    return render(request , 'shop/search.html')

def productview(request, myid):
    product = Product.objects.get(id = myid)

    return render(request , 'shop/prodview.html',{'product':product})

def checkout(request):
    return render(request , 'shop/checkout.html')
    
