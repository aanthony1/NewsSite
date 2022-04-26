from django.shortcuts import render

# Create your views here.
# Function that defines home html. Andre' Anthony 1/5/2021
# Add import to import API.  Andre` Anthony 1/5/2021
# Import JSON. Andre` Anthony 1/5/2021

def home(request):
    import requests
    import json
    news_api_request = requests.get(
                                    "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=08b0c3b9521c4036911206ef4313146b"

                                    )
    api = json.loads(news_api_request.content)
    
    return render(request, 'home.html', {'api': api})

