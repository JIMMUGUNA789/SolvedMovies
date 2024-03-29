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
    path('popular/movies/', views.popularMovies, name='popular_movies'),
    path('popular/tvshows/', views.popularTvShows, name='popular_tv'),
    path('detailsTv/<int:id>/', views.detailsTv, name='detailsTv'),
    path('trailers/', views.videoTrailers, name='videoTrailers'),
    path('tvseasons/<int:id>/', views.getSeasons, name='getSeasons'),
    path('contact/', views.contactUs, name='contact_us'),
    path('tvseasons/<int:id1>/<int:id2>/', views.getSeasonTrailers, name='get_season_trailers'),
    path('tvseasons/episodes/<int:tvid>/<int:seasonnumber>/', views.getEpisodes, name='episodes'),
    

]