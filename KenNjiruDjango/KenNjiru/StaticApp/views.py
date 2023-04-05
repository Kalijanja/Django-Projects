from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.

def static(request):
    return render(request, "static.html")
