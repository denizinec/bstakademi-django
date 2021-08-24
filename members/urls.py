from django.urls import path
from members import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login' , views.login_attempt , name="login"),
    path('register' , views.register_attempt , name="register"),
    path("logout_user", views.logout_user, name='logout_user'),
    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' ,views.error_page , name="error"),
    path('profile/<int:id>/' ,views.profileIndex , name="profile"),

   
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 