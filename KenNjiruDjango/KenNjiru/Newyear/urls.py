from django.urls import path
from . import views

urlpatterns = [
    path("newyear", views.test)
]
