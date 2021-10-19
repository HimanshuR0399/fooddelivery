from typing import Dict
from django import http
from django.contrib import auth
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse,FileResponse
from fooddelivery import models
from random import shuffle
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homepage(request):
    query = models.Foods.objects.all()
    # shuffle(query)
    print(query[0])
    context = {
        'foods' : query
    }
    return render(request,'homepage.html',context)

def image(request,img):
    img = open("fooddelivery/images/"+img,'rb')
    return FileResponse(img)

def food(request,id):
    context = dict()
    context['food'] = models.Foods.objects.get(id = id)
    return render(request,"product.html",context)

def search(request):
    context = dict()
    query_set = models.Foods.objects.all()
    context['search'] = str()
    if request.POST.get('search') != '':
        query_set = query_set.filter(name__contains = request.POST.get('search').title())
        context['search'] = request.POST.get('search')
    context['protien'] = 0
    try:
        if request.POST.get('Fprotien') == 'on':
            query_set = query_set.filter(protien__lte = request.POST.get('protien'))
            context['protien'] = request.POST.get('protien')
    except:
        pass
    context['carb'] = 0
    try:
        if request.POST.get('Fcarb') == 'on':
            query_set = query_set.filter(carbs__lte = request.POST.get('protien'))
            context['carb'] = request.POST.get('protien')
    except:
        pass
    context['fat'] = 0
    try:
        if request.POST.get('Ffat') == 'on':
            query_set = query_set.filter(fats__lte = request.POST.get('fat'))
            context['fat'] = request.POST.get('fat')
    except:
        pass
    context['cal'] = 0
    try:
        if request.POST.get('Fcal') == 'on':
            query_set = query_set.filter(calorie__lte = request.POST.get('cal'))
            context['cal'] = request.POST.get('cal')
    except:
        pass
    context['data'] = str([{
        'length' : query_set.count(),
        'name' : [i.name for i in query_set],
        'chef_name' : [i.chef.name for i in query_set],
        'id' : [i.id for i in query_set],
        'photo' : [i.photo for i in query_set],
        'prise' : [i.prise for i in query_set]

    }])
    
    return render(request,'search.html',context)

def add_to_cart(request):
    if request.user.is_anonymous:
        request.session['next'] = request.META.get('HTTP_REFERER')
        redirect('login')
    else:
        cart  = models.Cart.objects.get(user = models.Users.objects.get(username = request.user.username),food = models.Foods.objects.get(id = request.POST.get('id')))
        if cart.count() == 0:
            new_item = models.Cart()
            new_item.user = models.Users.objects.get(username = request.user.username)
            new_item.food = models.Foods.objects.get(id = request.POST.get('id'))
            new_item.save()
            return HttpResponse('Item has been added to the cart')
        return HttpResponse('This item is already present in the cart')


def login_signup(request):
    context = dict()
    if request.method == 'POST':
        if request.POST.get('type') == 'signup':
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            contact = request.POST.get('contact')
            if len(contact) != 10 or not(contact.isnumeric()):
                return render(request,'login.html',{'message':"Invalid Contact number"})
            if models.Users.objects.filter(contact = contact).count() != 0:
                return render(request,'login.html',{'message':"The contact number is already present in the database"})
            username = request.POST.get('username')
            if username == '':
                return render(request,'login.html',{'message':"Username cannot be blank"})
            if models.Users.objects.filter(username= username).count() != 0:
                return render(request,'login.html',{'message':"Entered username is already taken by other user"})
            password = request.POST.get('password')
            cpassword  = request.POST.get('cpassword')
            if password != cpassword :
                return render(request,'login.html',{'message':"The password and confirm password didn't matched"})
            user = models.Users()
            auth_user = User.objects.create_user(username = username,password = password)
            auth_user.save()
            user.username = username
            user.name = name
            user.gender = gender
            user.contact = contact
            user.save()
            return render(request,'login.html',{'message':"The user has been registered successfully"})
        elif request.POST.get('type') == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request,username = username,password = password)
            print(user)
            if user is not None:
                login(request,user)
                try: 
                    return redirect(request.session['next'])
                except:
                    return redirect('/')
            return render(request,'login.html',{'message':"Incorrect username or password"})
    



    return render(request,'login.html',context)


def cart(request):
    return render(request,'cart.html')