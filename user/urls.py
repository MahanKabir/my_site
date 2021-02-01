
from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name='register') #localhost:8000/accounts/register
]