from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('image/<str:img>',views.image,name = 'image'),
    path('search/',views.search,name = 'search'),
    path('food/<int:id>',views.food,name = "food"),
    path('add_to_cart',views.add_to_cart,name="add_to_cart"),
    path('login',views.login_signup,name= "login"),
    path('cart',views.cart,name= "cart"),
    path("checkout",views.checkout,name = "checkout")
]