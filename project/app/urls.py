from django.urls import path
from .views import *
from .views import addtocart

urlpatterns=[


    path('',home,name='home'),
    path('shop/',shop,name='shop'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('cart/',cart,name='cart'),
    path('addproduct/',addproduct,name='addproduct'),
    path('addedproduct/',addedproduct,name='addedproduct'),
    # path('singlecart/<int:pk>',singlecart,name='singlecart'),
    path('addtocart/<int:pk>',addtocart,name='addtocart'),
    path("deletecart/<int:pk>",deletecart,name='deletecart'),
    path("checkout/",checkout,name='checkout'),
    path("payment/",payment,name='payment'),
    path('payment-status', payment_status, name='payment-status'),




]

# Ensure media files are served during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)