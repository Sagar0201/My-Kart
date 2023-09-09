from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(ProductCat)
admin.site.register(ProductInfo)
admin.site.register(RatingReview)
admin.site.register(Cart)
admin.site.register(ProductHistory)