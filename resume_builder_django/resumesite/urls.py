from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.home, name="home"),
    path('informal/',views.info,name="info"),
    path('', views.homepage, name="homepage"),
    path('formal/', views.formal, name="formal"),
   
]
