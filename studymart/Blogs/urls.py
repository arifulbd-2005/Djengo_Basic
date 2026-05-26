from django.urls import path
from . import views

urlpatterns = [
    path('b1/',views.blog1),
    path('b2/',views.blog2)
]