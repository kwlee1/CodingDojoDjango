# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display a new from to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request):
    response = 'placeholder to display blog {{number}}'
    return HttpResponse(response)

def edit(request):
    response = 'placeholder to edit blog {{number}}'
    return HttpResponse(response)
    
def destroy(request):
    return redirect('/blogs')

# Create your views here.
