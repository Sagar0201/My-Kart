from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserDetails(models.Model):

     kart_user = models.OneToOneField(User,on_delete=models.CASCADE )

     mobile_number = models.BigIntegerField(default=123456789)

     gender = models.CharField(choices=(('M','Male'),('F','Female'),('C','Custom')),default='C',max_length=1)

     date_of_birth = models.DateField()
     
     is_seller = models.BooleanField(default=False)
     
     address = models.CharField(max_length=255)
     pin_code = models.IntegerField()
     
     
     created_at = models.DateTimeField(auto_now=True)
     updated_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return f'{self.kart_user.username} - {self.mobile_number}'
     
     
     
class ProductCat(models.Model):
     name = models.CharField(max_length=255)
     
     created_at = models.DateTimeField(auto_now=True)
     updated_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return self.name
     
     
class ProductInfo(models.Model):
     
     name = models.CharField(max_length=255)
     category = models.ForeignKey(ProductCat,on_delete= models.CASCADE)
     price = models.DecimalField(max_digits=8,decimal_places=2)
     price_after_discount = models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
     discount =  models.IntegerField()
     quantity = models.IntegerField()
     info = models.TextField()
     product_img = models.ImageField(upload_to ='ProductImgs',null=True,blank=True)
     is_show = models.BooleanField(default=True)
     duration = models.IntegerField()
     
          
     created_at = models.DateTimeField(auto_now=True)
     updated_at = models.DateTimeField(auto_now_add=True)
     
     
     def __str__(self):
          return self.name
     


class RatingReview(models.Model):
     product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
     kart_user = models.ForeignKey(User,on_delete=models.CASCADE)
     rating = models.IntegerField()
     review = models.CharField(max_length=255)
     product_img= models.ImageField(upload_to ='ReviewProduct',null=True,blank=True)
     
     created_at = models.DateTimeField(auto_now=True)
     updated_at = models.DateTimeField(auto_now_add=True)
     
     
     
     
class Cart(models.Model):
     kart_user = models.ForeignKey(User,on_delete=models.CASCADE)
     product = models.ForeignKey(ProductInfo,on_delete=models.CASCADE)
     
     created_at = models.DateTimeField(auto_now=True)
     updated_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return f'{product.name} {kart_user.username}'  
     
     
     
class ProductHistory(models.Model):
     kart_user = models.ForeignKey(User,on_delete=models.CASCADE)
     product = models.ForeignKey(ProductInfo,on_delete=models.CASCADE)
     
     created_at = models.DateTimeField(auto_now=True)
     updated_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return f'{product.name} {kart_user.username}'  
     