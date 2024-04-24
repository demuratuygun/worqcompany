from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.getUser),
    path('user/add/', views.addUser),
    path('platform/', views.getPlatform),
    path('platform/add/', views.addPlatform),

]