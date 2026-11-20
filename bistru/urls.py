from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'bistru'

urlpatterns = [
    path("", views.entrar, name="bistru"),
    path('entrar/', views.entrar, name='entrar'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path("redirecionar/", views.rotas_login, name="rotas_login"),
    path("sair/", views.sair, name="sair"),

    #recuperação de senha
    #página para enviar e-mail
    #enviar código ou link?
    path("recuperar/", auth_views.PasswordResetView.as_view(template_name="bistru/recuperar.html"), name="recuperar")


]