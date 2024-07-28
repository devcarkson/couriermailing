from django.urls import path 

from . import views

from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('express/', views.express, name='express'),
    path('normal/', views.normal, name='normal'),
    path('oceanfreight/', views.oceanfreight, name='oceanfreight'),
    path('airfreight/', views.airfreight, name='airfreight'),
    path('roadfreight/', views.roadfreight, name='roadfreight'),
    path('movements/', views.movements, name='movements'),
    path('importers/', views.importers, name='importers'),
    path('exports/', views.exports, name='exports'),
    path('logistics/', views.logistics, name='logistics'),
    path('contact/', views.contact, name='contact'),
    path('household/', views.household, name='household'),
    path('commercial/', views.commercial, name='commercial'),
    path('international/', views.international, name='international'),
    path('trackingDetails/', views.trackingDetails, name='trackingDetails'),
    path('domestic/', views.domestic, name='domestic'),
    path('forwarder/', views.forwarder, name='forwarder'),
    path('consultation/', views.consultation, name='consultation'),
    path('payment/', views.payment, name='payment'),
    path('payments/', views.payments, name='payments'),
    path('track/', track_number, name='track_number'),
]