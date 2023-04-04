from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

def test(request):
    now = datetime.datetime.now()
    return render(request, "newy.html", {
        "new": now.month == 1 and now.day == 1
    })
