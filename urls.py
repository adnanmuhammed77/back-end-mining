from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='login'),
    path('product',views.productpage,name='product'),
    path('about',views.about,name='about'),
    path('logout',views.logoutpage,name='logout')
    
]
