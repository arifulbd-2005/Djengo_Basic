from django.urls import path
from . import views

urlpatterns = [
    path('da/',views.data_analys, name='data'),
]