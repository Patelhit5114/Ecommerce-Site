from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    dict = { 'name' : 'blog'}
    return render(request,'blog/home.html',dict)

