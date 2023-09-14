"""
URL configuration for cservice project.

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
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('services/add', views.addService, name='addService'),
    path('services/update/<int:serviceId>/', views.updateService, name='updateService'),
    path('services/delete/<int:serviceId>/', views.deleteService, name='deleteService'),
    path('testimonials/add', views.addTestimonial, name='addTestimonial'),
    path('testimonials/update/<int:testimonialId>/', views.updateTestimonial, name='updateTestimonial'),
    path('testimonials/delete/<int:testimonialId>/', views.deleteTestimonial, name='deleteTestimonial'),
    path('updateInformation', views.updateInformation, name='updateInformation'),
    path('services', views.services, name='services'),
    path('services/send-message', views.sendMessage, name='sendMessage'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('feedback/<str:email>/', views.feedback, name='feedback'),
    path('feedback/add', views.addFeedback, name='addFeedback'),
    path('admin/', admin.site.urls),
]
