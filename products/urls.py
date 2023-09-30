from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path("",views.home,name="home"),
     path("signup/",views.signup,name="signup"),
     path("login/",views.login,name="login"),
     
     path('add-product/',views.add_product,name="add_product"),
     path('search/',views.search,name='search'),
     path('product/<int:id>',views.product_item,name="product_item"),
     
     path('rating-review/',views.rating_review, name='rating_review'),
     path('cart',views.cart,name="cart"),
     
     
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)