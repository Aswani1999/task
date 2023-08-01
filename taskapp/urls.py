from django.contrib import admin
from django.urls import path, include

from taskapp import views

urlpatterns = [
    path('',views.demo,name="demo"),

]