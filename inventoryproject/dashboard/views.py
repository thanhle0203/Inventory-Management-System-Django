from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1 style="color:red;"> This is the index Page </h1>')

def staff(request):
    return HttpResponse('This is the staff Page')