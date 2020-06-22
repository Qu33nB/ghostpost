from django.urls import path
from ghostposts import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/', views.add_ghost_post),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
]