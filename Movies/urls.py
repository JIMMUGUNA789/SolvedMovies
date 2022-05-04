from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies, name='getmovies'),
    path('detail/<int:id>/', views.details, name='details'),
]