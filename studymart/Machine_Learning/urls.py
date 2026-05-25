from django.urls import path
from . import views

urlpatterns = [
    path('ml/',views.machine_learning),
    path('rn/',views.rendom_forest),
    path('kn/',views.k_nearest),
    path('dt/',views.dtree),
]