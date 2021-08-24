from django.urls import path
from . import views

#127.0.0.1:8000/movies
#127.0.0.1:8000/movies/2
#127.0.0.1:8000/movies/search

urlpatterns = [
    path('', views.pollsIndex, name = 'pollsIndex'),#boş sayfa geçdiğinde index geçsin
    path('/projectidea/<int:pk>', views.pollsDetail0, name = 'pollsDetail0'),
    path('/projectidea/<int:pk>/delete', views.pollsDelete0, name = 'pollsDelete0'),
    path('/week1/<int:pk>', views.pollsDetail, name = 'pollsDetail'),
    path('/week1/<int:pk>/delete', views.pollsDelete, name = 'pollsDelete'),
    path('/week2/<int:pk>', views.pollsDetail2, name = 'pollsDetail2'),
    path('/week2/<int:pk>/delete', views.pollsDelete2, name = 'pollsDelete2'),
    path('/week3/<int:pk>', views.pollsDetail3, name = 'pollsDetail3'),
    path('/week3/<int:pk>/delete', views.pollsDelete3, name = 'pollsDelete3'),
    path('/week4/<int:pk>', views.pollsDetail4, name = 'pollsDetail4'),
    path('/week4/<int:pk>/delete', views.pollsDelete4, name = 'pollsDelete4'),
    path('/week5/<int:pk>', views.pollsDetail5, name = 'pollsDetail5'),
    path('/week5/<int:pk>/delete', views.pollsDelete5, name = 'pollsDelete5'),
    path('/week6/<int:pk>', views.pollsDetail6, name = 'pollsDetail6'),
    path('/week6/<int:pk>/delete', views.pollsDelete6, name = 'pollsDelete6'),
    path('/week7/<int:pk>', views.pollsDetail7, name = 'pollsDetail7'),
    path('/week7/<int:pk>/delete', views.pollsDelete7, name = 'pollsDelete7'),
    path('/week8/<int:pk>', views.pollsDetail8, name = 'pollsDetail8'),
    path('/week8/<int:pk>/delete', views.pollsDelete8, name = 'pollsDelete8'),
]