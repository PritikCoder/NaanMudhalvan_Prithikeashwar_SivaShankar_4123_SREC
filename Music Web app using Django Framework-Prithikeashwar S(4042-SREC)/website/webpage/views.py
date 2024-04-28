from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

#def display(request):
 #  return HttpResponse("welcome all")

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request , 'signup.html')

def home(request):
   return render(request, 'home.html')

def songpage1(request):
   return render(request, 'songpage1.html')

def songpage2(request):
   return render(request, 'songpage2.html')

def songpage3(request):
   return render(request, 'songpage3.html')
