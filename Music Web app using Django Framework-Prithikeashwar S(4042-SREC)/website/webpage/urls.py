from .views import login, signup, home
from django.urls import path
from django import views
from webpage import views
from . import views
#from website import webpage

urlpatterns = [
   path('', views.home, name = 'home'),
   path("login/", views.login, name = 'login'),
   path("signup/", views.signup, name = 'signup'),
   path("songpage1/", views.songpage1, name = 'songpage1'),
   path("songpage2/", views.songpage2, name = 'songpage2'),
   path("songpage3/", views.songpage3, name = 'songpage3'),

]