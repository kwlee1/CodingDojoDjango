# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def register(request):
    response = 'placeholder for users to create a new user record'
    return HttpResponse(response)

def login(request):
    response = 'placeholder for users to login'
    return HttpResponse(response)

def new(request):
    return redirect('/register')

def index(request):
    response = 'placeholder to display all the list of users'
    return HttpResponse(response) 


# Create your views here.
