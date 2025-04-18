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


@login_required
def marcar_favorito(request, video_id):
    if request.method == "POST":
        url = "https://www.googleapis.com/youtube/v3/videos"
        params = {
            'key': settings.YOUTUBE_API_KEY,
            'part': 'snippet',
            'id': video_id,
        }
        response = requests.get(url, params=params)
        data = response.json()

        try:
            snippet = data['items'][0]['snippet']
            titulo = snippet['title']
            thumbnail = snippet['thumbnails']['medium']['url']
        except (IndexError, KeyError):
            return HttpResponse("No se pudo obtener la información del video.", status=400)

        # Guardar favorito
        VideoFavorito.objects.get_or_create(
            user=request.user,
            video_id=video_id,
            defaults={
                'titulo': titulo,
                'thumbnail_url': thumbnail,
            }
        )
        return redirect('home')

@login_required
def ver_favoritos(request):
    favoritos = VideoFavorito.objects.filter(user=request.user)
    return render(request, 'videos/favoritos.html', {'favoritos': favoritos})

@login_required
def desmarcar_favorito(request, video_id):
    VideoFavorito.objects.filter(user=request.user, video_id=video_id).delete()
    return redirect('ver_favoritos')