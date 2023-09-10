from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import auth

# Create your views here.


# def validate(type,value):
     
#      if type == 'mobile_number':
          
#           if len(str(value)) == 10:
#                return True
#           else:
#                return False



def home(request):
     return render(request,'basic.html')

def signup(request):
     
     
     if request.method == "POST":
          print(request.POST)
          
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username= request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          
          
          mobile_number = request.POST['mobile_number']
          
          # if len(str(mobile_number)) != 10:
          #      messages.error(request,'Invalid mobile number')
          #      return redirect('signup')
          
          # if not validate('mobile_number',mobile_number) :
          #      messages.error(request,'invalid number')
          #      return redirect('signup')
          
          
          gender = request.POST['gender']
          date_of_birth = request.POST['date_of_birth']
                              
          address = request.POST['address']
          pin_code = request.POST['pin_code']
          
          if request.POST['user_type'] == "True":
               is_seller = True
          else:
               is_seller = False
          
          
          try:
               user_info = User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
               
          except:
               messages.error(request, "Invalid Username")
               return redirect('signup')
          
          try:
               
               UserDetails.objects.create(kart_user = user_info,mobile_number=mobile_number,gender=gender,date_of_birth=date_of_birth,address=address,pin_code=pin_code)

               messages.success(request, "Your account has been Created")
               
               return redirect('signup')
          
          except:
               messages.error(request, "sorry something went wrong")
               return redirect('signup')
     
     
     return render(request,'account/signup.html')



def login(request):
     
     if request.method == "POST":
          
          username = request.POST['username']
          password = request.POST['password']
          
          user = authenticate(username=username,password=password)

          
          if user is not None:

               if user.is_active:
                    auth.login(request,user)
                    return redirect('home')
               else:
                    messages.error(request,'user is not active')
                    return redirect('login')
          else:
               messages.error(request,'Invalid Username or Password')
               return redirect('login')
               
          
     
     return render(request,'account/login.html')
