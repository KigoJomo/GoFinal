
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>/', views.delete),
    path('contact/', views.contact, name='contact'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
]
