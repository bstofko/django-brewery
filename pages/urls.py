from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('list/', views.list, name="list"),
    path('search/', views.search, name="search")
]
