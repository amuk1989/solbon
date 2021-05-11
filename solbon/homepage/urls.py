from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_index),
    path('<int:pk>/', views.new_index),
]
