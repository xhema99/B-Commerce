from django.urls import path

from . import views

app_name = 'comunicacion'

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja'),
    path('<int:pk>/', views.detalles, name='detalles'),
    path('new/<int:libro_pk>/', views.nuevo_chat, name='nuevo'),
]