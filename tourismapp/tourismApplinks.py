from django.urls import path
from .views import signinpage 
from .views import signuppage
from .views import homepage
urlpatterns=[
    path("signinpage/", signinpage, name="signinpage"),
    path("signuppage/", signuppage, name="signuppage"),
    path("homepage/", homepage, name="homepage")
]