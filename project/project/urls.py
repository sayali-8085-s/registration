"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('register/',views.register,name ='register'),
    path('login/',views.login,name ='login'),
    # path('userdashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('userdashboard/', views.dashboard, name='dashboard'),


    # path('query/<int:pk>/', views.query, name='query'),
    path('userdashboard/query/<int:pk>/', views.query, name='query'),
    path('querydata/', views.querydata, name='querydata'),
    path('userdashboard/showquery/', views.showquery, name='showquery'),
    path('edit/<int:pk>/<int:pke>/', views.edit, name='edit'),
    path('updat/<int:pk>/<int:pke>/', views.updat, name='updat'),
    path('delete/<int:pk>/<int:pke>/', views.delete, name='delete'),

#    name related to url template related
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
