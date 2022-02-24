from django.contrib import admin
from django.urls import include, path, reverse
from . import views

urlpatterns = [
    path('test_tree', views.test_tree),
    path('test_static', views.test_static),
]