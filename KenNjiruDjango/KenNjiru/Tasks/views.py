from django.shortcuts import render

# Create your views here.

tasks = ["Buy Groceries", "Watch Football", "Visit a Friend"]


def test(request):
    return render(request, "tasks.html", {

        "tasks": tasks

    })

def add(request):
    return  render(request, "add.html")
