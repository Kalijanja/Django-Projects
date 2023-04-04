from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="Hello"),
    path("eMobilis", views.eMobilis, name="eMobilis"),
    path("home", views.home, name="Home"),
]
