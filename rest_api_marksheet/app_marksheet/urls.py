from django.contrib import admin
from django.urls import path
from app_marksheet import views

urlpatterns = [
    path("",views.index, name="index"),
    path("marks/<id>", views.marks, name="marks")

]