from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path("",views.home,name="home"),
     path("signup/",views.signup,name="signup"),
     path("login/",views.login,name="login"),
     
     path('add-product/',views.add_product,name="add_product"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)