from django.http import HttpResponse
import requests, os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import VideoFavorito

YOUTUBE_API_KEY = os.getenv("API_KEY")

@login_required
def home(request):
    query = request.GET.get('q', 'programación')
    r = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={YOUTUBE_API_KEY}')
    data = r.json()
    resultados = [
        {
            'id': item['id']['videoId'],
            'titulo': item['snippet']['title'],
            'thumbnail': item['snippet']['thumbnails']['medium']['url'],
        }
        for item in data.get('items', [])
        if item['id'].get('videoId')
    ]
    favoritos = VideoFavorito.objects.filter(user=request.user).values_list('video_id', flat=True)
    return render(request, 'videos/home.html', {'videos': resultados, 'favoritos': favoritos})