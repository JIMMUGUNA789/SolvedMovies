from django.shortcuts import render
from django.conf import settings
import  requests

apiKey = settings.API_KEY
BASE_URL = 'https://api.themoviedb.org/3/movie/'
def getMovies(request):
    # popular movies
    items = []
    urlPopular = BASE_URL+'popular'+apiKey
    response1 = requests.get(urlPopular)
    popular = response1.json()
    print (popular)
    items.extend(popular.results)
    


    # Now Playing movies
    urlNowPlaying = BASE_URL+'now_playing'+apiKey
    response2 = requests.get(urlNowPlaying)
    now_playing = response2.json()
    # print(now_playing)
    context={
        "popular":popular,
        "items":items,
        "now_playing":now_playing,
    }
    return render(request, 'index.html', context)


