from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import EmailForm


class IndexView(TemplateView):
    template_name = 'index.html'


class EmailView(FormView):
    template_name = 'email.html'
    form_class = EmailForm
    success_url = 'send_email'

    def form_valid(self, form):
        # フォームのデータを取得
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # メール送信
        send_mail(subject, message, email, ['riku.popo161209@gmail.com'])
        return super().form_valid(form)
    

class SendEmailView(TemplateView):
    template_name = 'send_email.html'


class FavoriteView(TemplateView):
    template_name = 'favorite.html'


class GameView(TemplateView):
    template_name = 'game.html'


class HobbyView(TemplateView):
    template_name = 'hobby.html'


class MangaView(TemplateView):
    template_name = 'manga.html'

    
class MusicView(TemplateView):
    template_name = 'music.html'
    
    
class NewsView(TemplateView):
    template_name = 'news.html'


class SportsView(TemplateView):
    template_name = 'sports.html'


