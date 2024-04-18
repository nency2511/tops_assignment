from django.contrib import admin
from django.urls import path,include
from app_api import views
from .views import*

urlpatterns = [

    path("product",productAPI.as_view()),
    path("book",bookAPI.as_view())
]