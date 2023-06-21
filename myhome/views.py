from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *

def home(request):
    ctg = Category.objects.all()
    tex ={
        'ctg':ctg
    }
    tex ={}
    return render(request, 'blog/index.html',tex)

def cart(request):
    
    tex ={}
    return render(request, 'blog/cart.html',tex)


def checkout(request):
    tex ={}
    return render(request, 'blog/checkout.html',tex)


def detail(request):
    tex ={}
    return render(request, 'blog/detail.html',tex)


def shop(request):
    tex ={}
    return render(request, 'blog/shop.html',tex)


def  contact(request):
    tex ={}
    return render(request, 'blog/contact.html',tex)

def base(request):
    ctg = Category.objects.all()
    tex ={
        'ctg':ctg
    }
    return render(request, 'base.html',tex)
