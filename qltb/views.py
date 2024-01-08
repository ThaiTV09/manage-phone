from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def home(request):
    context={}
    return render(request,'app/home.html',context)

def base(request):
    context={}
    return render(request,'app/base.html',context)