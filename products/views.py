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



def add_product(request):
     
     user_info = request.user
     user_extra_info = UserDetails.objects.get(kart_user_id = user_info.id)

     
     if not user_extra_info.is_seller:
          messages.warning(request,'you are not a seller')
          return redirect('home')
     
     category = ProductCat.objects.all()
     
     
     if request.method == "POST":
          
          name= request.POST['name']
          category= request.POST['category']
          price= request.POST['price']
          discount= request.POST['discount']
          quantity= request.POST['quantity']
          info= request.POST['info']
          duration= request.POST['duration']
          
          product_img = request.FILES['product_img']
          is_show = request.POST['is_show']
          
          if is_show == "True":
               is_show = True
          else:
               is_show == False
               
               
          price_after_discount =float(price)- (float(price) * float(discount))/100
               
          
          
          try:
               ProductInfo.objects.create(name=name,category_id =category,price=price,discount=discount,quantity=quantity,info=info,duration=duration,product_img=product_img,is_show=is_show,price_after_discount=price_after_discount)
               messages.success(request,'product added')
               return redirect('add_product')
          except:
               messages.error(request,'something went wrong')
               return redirect('add_product')
     
     
     
     
     return render(request,'products/add_product.html',{"categories":category})


def home(request):
     
     
     categories= ProductCat.objects.all()
     
     
     product_by_cat =[]
     
     
     for cat in categories:
          
          products= ProductInfo.objects.filter(category_id =cat.id )
          
          if products.exists():
               product_data={'product_cat':cat.name,'product_info':products}
               product_by_cat.append(product_data)
               
     
     
     return render(request,'products/index.html',{'categories':product_by_cat})






def search(request):
     
     query = request.GET.get('query')
     
     
     name = ProductInfo.objects.filter(name__icontains=query)
     category= ProductInfo.objects.filter(category__name__icontains=query)
     price= ProductInfo.objects.filter(price__icontains=query)
     info= ProductInfo.objects.filter(info__icontains=query)
     
     
     search_results = name.union(category,price,info)
     
     
     return render(request,'products\search.html',{'search_results':search_results,'query':query})
     
     
def product_item(request,id):
     
     try:
          product=ProductInfo.objects.get(id=id)
          reviews = RatingReview.objects.filter(product_id =id)
          rating_review_count= reviews.count()
          final_rating = 0
          for i in reviews:
               final_rating += i.rating
          if rating_review_count != 0:
               final_rating = final_rating / rating_review_count
          else:
               final_rating = 0
          return render(request,'products\product_item.html',{'product':product,'reviews':reviews,'final_rating':final_rating,'rating_review_count':rating_review_count})
     except:
          messages.error(request,'data not found')
          return redirect('home')
     
     
     
def rating_review(request):
     
     if request.method == 'POST' and  request.user is not None :
          
          product_id = request.POST['product_id']
          rating = request.POST['rating']
          review = request.POST['review']
          product_img = request.FILES['product_img']
          
          user_id = request.user.id
          try:
               RatingReview.objects.create(product_id = product_id,kart_user_id = user_id,rating=rating,review=review,product_img=product_img)
               messages.success(request,'rating and review added')
               return redirect(f'/product/{product_id}')
          
          except:
               messages.error(request,'something went wrong')
               
          
     else:
          messages.error(request,'rating and review not added')
          return redirect('home')
          
          
          
def cart(request):
     
     if request.method == "POST":
          
          product_id  = request.POST['product_id']
          action  = request.POST['action']
          
          
          user_id = request.user.id
          
          cart_item = Cart.objects.filter(kart_user_id = user_id,product_id = product_id)
          
          if cart_item.count() == 0:
               try:
                    
                    Cart.objects.create(kart_user_id = user_id,product_id = product_id)
                    messages.success(request,'product added into cart')
                    
               except:
                    messages.error(request,"something went wrong")
               
          else:
               
               if action =='delete':
                    try:
                         cart=Cart.objects.get(product_id= product_id) 
                         cart.delete()
                         messages.success(request,'product remove in cart')
                    except:
                         messages.error(request,"something went wrong")
               else:
                    messages.warning(request,'product already exits in cart')
                    return redirect(f"/product/{product_id}")
     
     
          
     user_id = request.user.id
     
     cart_items = Cart.objects.filter(kart_user_id =user_id)
     total_items = cart_items.count()
     
     total_price =0
     final_price = 0
     
     
     for item in cart_items:
          total_price += item.product.price
          final_price += item.product.price_after_discount
     
     discount_price = total_price - final_price

          
          
     return render(request,'products\cart.html',{'cart_items':cart_items,'total_items':total_items,'total_price':total_price,'final_price':final_price,'discount_price':discount_price})
     