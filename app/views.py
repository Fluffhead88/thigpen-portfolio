from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("This is Zachary Thigpen's Portfolio")
