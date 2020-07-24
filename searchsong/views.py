from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchForm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import SearchBar
from django.http import HttpResponse

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"
    search = SearchForm()

    def get(self, request, *args, **kwargs):
        context = {
            'search': self.search
        }
        return render(request, 'index.html', context = context)

client_id = "b6dc7002932340799f70f873d6059abb"
client_secret = "c4188f8315f0473db913d84f67251630"

def idGenerator(search):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API
    names = search #chosen artist
    result = sp.search(names) #search query
    if result['tracks']['items'][0]['artists'][0]['name'] == 'names' :
        id =  result['tracks']['items'][0]['artists'][0]['id']
        type = result['tracks']['items'][0]['artists'][0]['type']
        return type, id
    elif result['tracks'] ['items'] [0] ['type'] == 'album' :
        id =  result['tracks']['items'][0]['id']
        type = result['tracks']['items'][0]['type']
        return type, id
    elif result['tracks'] ['items'] [0] ['type'] == 'track' :
        id =  result['tracks']['items'][0]['artists'][0]['id']
        type = result['tracks']['items'][0]['artists'][0]['type']
        return type, id
    else:
        id = "Not"
        type = "found"
        return type, id

def searchbar(request):
    search_query = SearchForm(request.POST or None)
    if request.method == "POST":
        search_result = search_query.save(commit = False)
        search_result.save()
        key, value = idGenerator(search_result.search)
        if key=="Not":
            return 
        context = {
            'key': key,
            'value': value
        }

    return render(request, 'search.html', context)
