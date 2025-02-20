from django.urls import path
from .views import signinpage 
from .views import signuppage
urlpatterns=[
    path("signinpage/", signinpage, name="signinpage"),
    path("signuppage/", signuppage, name="signuppage"),
]