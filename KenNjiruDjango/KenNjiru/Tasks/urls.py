from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path('', views.test, name="tasks"),
    path('add/', views.add, name="add")
]
