from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return HttpResponse ('Welcome to Emobilis')
def About(request):
    return HttpResponse ('About Emobilis')
def Services(request):
    return HttpResponse ('Emobilis Services')
