from typing import Dict
from django import http
from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from fooddelivery import models
from random import shuffle
from django import forms

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
    food = models.Foods.objects.get(id = id)
    context = {
        'name' : food.name
        
    }

def search(request):
    print(request.POST)
    context = dict()
    query_set = models.Foods.objects.all()
    context['search'] = str()
    print(query_set)
    if request.POST.get('search') != '':
        query_set = query_set.filter(name__contains = request.POST.get('search').title())
        context['search'] = request.POST.get('search')
    context['protien'] = 0
    print(query_set.count())
    print(request.POST.get('Fprotien'),type(request.POST.get('Fprotien')))
    try:
        if request.POST.get('Fprotien') == 'on':
            query_set = query_set.filter(protien__lte = request.POST.get('protien'))
            context['protien'] = request.POST.get('protien')
            print('prot')
    except:
        pass
    print(query_set.count())
    context['carb'] = 0
    try:
        if request.POST.get('Fcarb') == 'on':
            query_set = query_set.filter(carbs__lte = request.POST.get('protien'))
            context['carb'] = request.POST.get('protien')
            print('carb')
    except:
        pass
    print(query_set.count())
    context['fat'] = 0
    try:
        if request.POST.get('Ffat') == 'on':
            query_set = query_set.filter(fats__lte = request.POST.get('fat'))
            context['fat'] = request.POST.get('fat')
            print('fat')
    except:
        pass
    print(query_set.count())
    context['cal'] = 0
    try:
        if request.POST.get('Fcal') == 'on':
            query_set = query_set.filter(calorie__lte = request.POST.get('cal'))
            context['cal'] = request.POST.get('cal')
            print('cal')
    except:
        pass
    print(query_set.count())
    context['data'] = query_set
    
    return render(request,'search.html',context)
