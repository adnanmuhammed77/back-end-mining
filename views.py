from audioop import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
  return render(request,'index.html')
def loginpage(request):
  if request.method=='POST':
    username=request.POST.get('username')
    pass1=request.POST.get('pass')
    user=authenticate(request,username=username,password=pass1)
    if user is not None:
       login(request,user)
       return redirect('product')
    else:
      # return HttpResponse("username or password is incorrect")
      messages.error(request,'invalid username and password!!!')


  return render(request,'login.html')
def register(request):
  if request.method=='POST':
    uname=request.POST.get('username')
    email=request.POST.get('email')
    pass1=request.POST.get('password1')
    pass2=request.POST.get('password2')

    if pass1!=pass2:
      # return HttpResponse("your passoword and conform password are not same")
      messages.error(request,'password and conform password are not same! ')
      return redirect('register')
    else:
      my_user=User.objects.create_user(uname,email,pass1)
      my_user.save()
    return redirect('login')
  return render(request,'register.html')
def productpage(request):
   pro=product.objects.all()
   return render(request,'product.html',{'products':pro})
def about(request):
  return render(request,'about.html')
def logoutpage(request):
  logout(request)
  return redirect('index')