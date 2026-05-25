"""
URL configuration for studymart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# old modify @............
"""from django.contrib import admin
from django.urls import path
from Machine_Learning import views as ml
from About_Us import views as about
from Blogs import views as b
from Deep_Learning import views as dl
from Data_Analysis import views as data"""

# old advance code @.........
"""from django.contrib import admin
from django.urls import path
from Machine_Learning.views import machine_learning
from Machine_Learning.views import deep_learning
from About_Us.views import about_us
from Blogs.views import blog1
from Data_Analysis.views import data_analys
from Deep_Learning.views import deep_learning"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('machine/', include('Machine_Learning.urls')),
    path('about/', include('About_Us.urls')),
    path('blog/', include('Blogs.urls')),
    path('deep/', include('Deep_Learning.urls')),
    path('data/', include('Data_Analysis.urls')),

]