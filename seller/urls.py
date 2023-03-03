from django.urls import path
from .views import *

urlpatterns = [
    path('seller_index/',seller_index, name='seller_index'),
    path('seller_header/',seller_header, name='seller_header'),
    path('seller_app_profile/',seller_app_profile, name='seller_app_profile'),
    path('seller_app_email/',seller_app_email, name='seller_app_email'),
    path('seller_page_login/',seller_page_login, name='seller_page_login'),
    path('seller_logout/',seller_logout, name='seller_logout'),
    path('seller_page_register/',seller_page_register, name='seller_page_register'),
    path('seller_add_product/',seller_add_product, name='seller_add_product'),
    path('my_product/',my_product, name='my_product')
]    