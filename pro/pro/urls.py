"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from pro.views import home
from django.conf import settings
from django.conf.urls.static import static
from pro.views import home
from pro.views import home1
from pro.views import home2
from pro.views import home3
from pro.views import home4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('index.html',home),
    path('about.html',home1),
    path('contact.html',home2),
    path('land.html',home3),
    path('signup.html',home4),


    

]
