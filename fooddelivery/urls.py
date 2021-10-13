from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('image/<str:img>',views.image,name = 'image'),
    path('search/',views.search,name = 'search'),
    path('food/<int:id>',views.food,name = "food")
]