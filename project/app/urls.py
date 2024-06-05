from django.urls import path
from .views import *

urlpatterns=[


    path('',home,name='home'),
    path('shop/',shop,name='shop'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('cart/',cart,name='cart'),

]