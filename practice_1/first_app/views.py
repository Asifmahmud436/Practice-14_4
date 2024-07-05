from django.shortcuts import render
from .forms import Practice_day1

def home(request):
    return render(request,"home.html")

def Practice_form1(request):
    form = Practice_day1()
    return render(request,'practice_day1.html',{'form':form})

