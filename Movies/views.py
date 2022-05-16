from multiprocessing import context
from django.shortcuts import render
from django.conf import settings
import requests

apiKey = settings.API_KEY
BASE_URL = "https://api.themoviedb.org/3/movie/"

# get all categories
urlCategories = "https://api.themoviedb.org/3/genre/movie/list" + apiKey
responseCategory = requests.get(urlCategories)
categories = responseCategory.json()


def getMovies(request):
    # popular movies

    urlPopular = BASE_URL + "popular" + apiKey
    response1 = requests.get(urlPopular)
    popular = response1.json()
    print(popular)

    # Now Playing movies
    urlNowPlaying = BASE_URL + "now_playing" + apiKey
    response2 = requests.get(urlNowPlaying)
    now_playing = response2.json()
    # print(now_playing)

    # upcoming
    urlUpcoming = BASE_URL + "upcoming" + apiKey
    response3 = requests.get(urlUpcoming)
    upcoming = response3.json()

    # animations
    DISCOVER_BASE_URL = "https://api.themoviedb.org/3/discover/movie"
    urlAnimations = DISCOVER_BASE_URL + apiKey + "&with_genres=16"
    response4 = requests.get(urlAnimations)
    animations = response4.json()
    # search functionality

    context = {
        "popular": popular,
        "now_playing": now_playing,
        "upcoming": upcoming,
        "animations": animations,
        "categories": categories,
    }
    return render(request, "index.html", context)


def details(request, id):
    strId = str(id)
    urlDetail = BASE_URL + strId + apiKey
    response = requests.get(urlDetail)
    movieDetail = response.json()

    # get cast
    urlCast = BASE_URL + strId + "/credits" + apiKey
    response1 = requests.get(urlCast)
    movieCast = response1.json()
    # print(movieCast)
    context = {
        "movieDetail": movieDetail,
        "movieCast": movieCast,
        "categories": categories,
    }
    return render(request, "detail.html", context)

    # specific category


def specificCategory(request, id):
    ID = str(id)
    url = "https://api.themoviedb.org/3/discover/movie" + apiKey + "&with_genres=" + ID
    genreData = requests.get(url)
    genreMovies = genreData.json()
    context = {
        "genreMovies": genreMovies,
    }
    return render(request, "genre.html", context)


def trailer(request, id):
    strId = str(id)
    url = BASE_URL + strId + apiKey + "&append_to_response=trailers"
    trailer = requests.get(url)
    trailers = trailer.json()
    print(trailers)
    context = {
        "trailers": trailers,
    }
    return render(request, "trailer.html", context)


def getAnimations(request):
    # animations
    DISCOVER_BASE_URL = "https://api.themoviedb.org/3/discover/movie"
    urlAnimations = DISCOVER_BASE_URL + apiKey + "&with_genres=16"
    response4 = requests.get(urlAnimations)
    animations = response4.json()
    context = {"animations": animations}
    return render(request, "animations.html", context)

# trending per day
def getTrendingDay(request):
    # movie
    trendingmovieurl = "https://api.themoviedb.org/3/trending/movie/day"+apiKey 
    response1=requests.get(trendingmovieurl)
    trendingmovies = response1.json()
    # tv
    trendingtvurl = "https://api.themoviedb.org/3/trending/tv/day"+apiKey 
    response2=requests.get(trendingtvurl)
    trendingtv = response2.json()
    # person
    # trendingpersonurl = "https://api.themoviedb.org/3/person/tv/day"+apiKey 
    # response3=requests.get(trendingpersonurl)
    # trendingperson = response3.json()
    context = {
        "trendingmovies":trendingmovies,
        "trendingtv":trendingtv,
        # "trendingperson":trendingperson,
    }
    return render(request, 'trending_day.html', context)

def getTrendingWeek(request):
    # movie
    trendingmovieurl = "https://api.themoviedb.org/3/trending/movie/week"+apiKey 
    response1=requests.get(trendingmovieurl)
    trendingmovies = response1.json()
    # tv
    trendingtvurl = "https://api.themoviedb.org/3/trending/tv/week"+apiKey 
    response2=requests.get(trendingtvurl)
    trendingtv = response2.json()
    # person
    # trendingpersonurl = "https://api.themoviedb.org/3/person/tv/week"+apiKey 
    # response3=requests.get(trendingpersonurl)
    # trendingperson = response3.json()
    context = {
        "trendingmovies":trendingmovies,
        "trendingtv":trendingtv,
        # "trendingperson":trendingperson,
    }
    return render(request, 'trending_week.html', context)


