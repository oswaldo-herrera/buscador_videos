from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('favoritos/', views.ver_favoritos, name='ver_favoritos'),
    path('marcar/<str:video_id>/', views.marcar_favorito, name='marcar_favorito'),
    path('desmarcar/<str:video_id>/', views.desmarcar_favorito, name='desmarcar_favorito'),
]