from django.urls import path
from . import views

urlpatterns = [
    path('b1/',views.blog1, name='blog1'),
    path('b2/',views.blog2, name='blog2'),
]