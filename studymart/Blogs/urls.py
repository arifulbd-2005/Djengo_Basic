from django.urls import path
from . import views

urlpatterns = [
    path('b1/',views.blog1, name='b1'),
    path('b2/',views.blog2, name='b2'),
    path('fm/',views.showformsdata, name='fm'),
]