from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

# Create your views here.
def home(request):
    title=[
        {"title":"Post 1","content":"kjdfhgjdfhkldjdfklj"},
        {"title":"Post 2","content":"kjdfhgjdfhkldjdfklj"},
        {"title":"Post 3","content":"kjdfhgjdfhkldjdfklj"},
        {"title":"Post 4","content":"kjdfhgjdfhkldjdfklj"},
        {"title":"Post 5","content":"kjdfhgjdfhkldjdfklj"},
        {"title":"Post 6","content":"kjdfhgjdfhkldjdfklj"}
    ]
    page_info={"title":"home","title_content":title}
    return render(request,"index.html",context=page_info)
 
def details(request):
    return render(request,"details.html")