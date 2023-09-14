from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('services/send-message', views.sendMessage, name='sendMessage'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('feedback/<str:email>/', views.feedback, name='feedback'),
    path('feedback/add', views.addFeedback, name='addFeedback'),
    path('admin/', admin.site.urls),
]
