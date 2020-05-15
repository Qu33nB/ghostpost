from django.urls import path
from ghostposts import views

urlpatterns = [
    path('', views.index),
    path('post/', views.ghost_post),
]