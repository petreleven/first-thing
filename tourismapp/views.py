from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
def signinpage(request):
    print("you did a"+request.method)
    if request.method=="POST":
         Username=request.POST.get("Username")
         Password=request.POST.get("Password")
         print(Username)
         print(Password)
         result=authenticate(username=Username, password=Password)
         if result == None:
              return HttpResponse ("You don't have an account.")
         else:
              login(request,result)
              return HttpResponse("Welcome!")
    return render(request, "signin.html")
def signuppage( request ):
     if request.method=="POST":
         Username=request.POST.get("Username")
         Password=request.POST.get("Password")
         Email=request.POST.get("Email")
         Firstname=request.POST.get("Firstname")
         Lastname=request.POST.get("Lastname")
         newPassword=make_password(Password)
         newUser=User(first_name=Firstname,
              last_name=Lastname,
              email=Email,
              password=newPassword,
              username=Username)
              
         print(Username)
         print(Password)
         print(Email)
         print(Firstname)
         print(Lastname)
         newUser.save()
     return render(request, "signup.html")





         