from django.shortcuts import render
from django.conf import settings
import  requests

apiKey = settings.API_KEY
BASE_URL = 'https://api.themoviedb.org/3/movie/popular?api_key='
def getMovies(request):
    url = BASE_URL+apiKey
    response = requests.get(url)
    data = response.json()
    print (data)
    context={
        "data":data
    }
    return render(request, 'index.html', context)


