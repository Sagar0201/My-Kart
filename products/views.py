from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.


def home(request):
     return render(request,'basic.html')

def signup(request):
     return render(request,'account/signup.html')
