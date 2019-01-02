from django.conf.urls import url
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/<slug>', views.Profile.as_view(), name='profile'),
]
