from django.contrib import admin
from django.urls import path
from app_myproduct import views

urlpatterns = [
    path("", views.Index, name="index"),
      path('delete/<id>',views.delete, name="delete"),
    path('update/<id>', views.update, name="update")
]