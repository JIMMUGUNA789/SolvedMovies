from django.shortcuts import render
from django.conf import settings
import  requests

apiKey = settings.API_KEY
BASE_URL = 'https://api.themoviedb.org/3/movie/'
def getMovies(request):
    # popular movies
    
    urlPopular = BASE_URL+'popular'+apiKey
    response1 = requests.get(urlPopular)
    popular = response1.json()
    # print (popular)
    
    


    # Now Playing movies
    urlNowPlaying = BASE_URL+'now_playing'+apiKey
    response2 = requests.get(urlNowPlaying)
    now_playing = response2.json()
    # print(now_playing)


    # upcoming
    urlUpcoming = BASE_URL+'upcoming'+apiKey
    response3 = requests.get(urlUpcoming)
    upcoming = response3.json()

    # animations
    DISCOVER_BASE_URL ='https://api.themoviedb.org/3/discover/movie'
    urlAnimations = DISCOVER_BASE_URL+apiKey+'&with_genres=16'
    response4 = requests.get(urlAnimations)
    animations = response4.json()







    context={
        "popular":popular,        
        "now_playing":now_playing,
        "upcoming":upcoming,
        "animations":animations,
    }
    return render(request, 'index.html', context)


