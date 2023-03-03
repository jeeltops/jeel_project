from  django.urls import path
from  .views import *


urlpatterns = [
    path('index/',index, name='index'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('cycle/',cycle, name='cycle'),
    path('news/',news, name='news'),
    path('add_row/',add_row, name='add_row'),
    path('register/',register, name='register'),
    path('login/',login,name='login'),
    path('otp/',otp, name='otp'),
    path('logout/',logout, name='logout')
]