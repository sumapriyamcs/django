from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

     path('name/' , views.hello),
     path('hello/' ,views.hello1),
     path('hi/', views.hii),

]