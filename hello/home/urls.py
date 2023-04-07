from django.contrib import admin
from django.urls import path
from home import views
from django.urls import include, path





urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services,name='services'),
    path("contact", views.contact, name='contact'),
    path('menu', views.menu_view, name='menu'),
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),  
    path('mc/', views.mc_view, name='mc'),
    path('scanner/', views.qr_scanner, name='qr_scanner'),
    path('place_order/', views.place_order, name='place_order'),

]



