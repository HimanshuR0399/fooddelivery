from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('image/<str:img>',views.image,name = 'image'),
    path('search/',views.search,name = 'search'),
    path('food/<int:id>',views.food,name = "food"),
    path('add_to_cart/<int:id>',views.add_to_cart,name="add_to_cart"),
    path('login',views.login_signup,name= "login"),
    path('cart',views.cart,name= "cart"),
    path('updatecart/<int:id>/<int:value>',views.update_cart,name= "chng_crt"),
    path('del_cart/<int:id>',views.del_cart,name="del_cart"),
    path('confirm_order',views.place_order,name="confirm_order"),
    path('payment/<int:order>',views.payment,name="payment"),
    # path("checkout",views.checkout,name = "checkout")
]