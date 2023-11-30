from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("email/", views.EmailView.as_view(), name="email"),
    path("email/send_email/", views.SendEmailView.as_view(), name="send_email"),
    path("favorite/", views.FavoriteView.as_view(), name="favorite"),
    path("game/", views.GameView.as_view(), name="game"),
    path("hobby/", views.HobbyView.as_view(), name="hobby"),
    path("manga/", views.MangaView.as_view(), name="manga"),
    path("music/", views.MusicView.as_view(), name="music"),
    path("news", views.NewsView.as_view(), name="news"),
    path("sports", views.SportsView.as_view(), name="sports"),
]