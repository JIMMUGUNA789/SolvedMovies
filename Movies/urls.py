from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies, name='getmovies'),
    path('detail/<int:id>/', views.details, name='details'),
    path('genre/<int:id>/', views.specificCategory, name='genre'),
    path('trailers/<int:id>/', views.trailer, name='trailers'),
    path('popular/animations/',views.getAnimations, name='get_animations'),
    path('trending/day/', views.getTrendingDay, name='trending_day'),
    path('trending/week/', views.getTrendingWeek, name='trending_week'),
]