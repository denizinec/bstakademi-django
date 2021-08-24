from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from app import urls

urlpatterns = [
    path('', views.user_proifle, name = 'user_profile'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 