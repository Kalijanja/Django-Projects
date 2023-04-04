from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

import datetime

from django.http import HttpResponse

def test(request):
    now = datetime.datetime.now()
    return render(request, 'Christy.html', {
        "new": now.month == 12 and now.day == 25
    })
