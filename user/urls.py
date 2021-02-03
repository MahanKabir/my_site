
from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'), #localhost:8000/accounts/register
    path('profile/', views.profile, name='profile'), #localhost:8000/accounts/profile
]


# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']