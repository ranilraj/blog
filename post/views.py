from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from .models import Post


# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,"index.html",context={"post":posts})
 
def details(request):
    return render(request,"details.html")