from django.urls import path
from . import views

urlpatterns = [
    path('dl/',views.deep_learning),
]