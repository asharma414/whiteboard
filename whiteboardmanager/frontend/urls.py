from django.urls import path
from . import views
urlpaterns = [
    path('', views.index)
]