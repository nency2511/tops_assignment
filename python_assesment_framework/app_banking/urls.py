from django.contrib import admin
from django.urls import path
from app_banking import views

urlpatterns = [
    path('',views.index, name="index"),
    path('reg',views.reg, name="reg"),
    path("info", views.info, name="info"),
    path('delete/<id>',views.delete, name="delete"),
    path('update/<id>', views.update, name="update"),
    path("customer", views.customer, name="customer"),

]