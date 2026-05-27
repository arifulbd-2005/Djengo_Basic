from django.urls import path
from . import views

urlpatterns = [
    path('ml/',views.machine_learning, name='ml'),
    path('rn/',views.rendom_forest, name='rn'),
    path('kn/',views.k_nearest,name='kn'),
    path('dt/',views.dtree, name='dt'),
]