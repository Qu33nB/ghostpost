from django.urls import path
from ghostposts import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/', views.add_ghost_post),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
    path('like/<int:id>/', views.likes),
    path('dislike/<int:id>/', views.dislikes),
    path('most-liked/', views.most_liked),
    path('least_liked/', views.least_liked),
]