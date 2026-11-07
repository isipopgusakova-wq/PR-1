from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('how-to-find/', views.how_to_find, name='how_to_find'),
    path('catalog/', views.catalog, name='catalog'),
]