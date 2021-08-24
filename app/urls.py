from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.newsIndex, name = 'newsIndex'),
    path('addnew', views.createNew, name = 'addnew'),
    path('dnew', views.ndashboard, name = 'dnew'),
    path('updateN/<int:id>/',views.updateNew, name = "updateN"),
    path('deleteN/<int:id>/',views.deleteNew, name = "deleteN"),
    path('addblog', views.createBlog, name = 'addblog'),
    path('dblog', views.bdashboard, name = 'dblog'),    
    path('updateB/<int:id>/',views.updateBlog, name = "updateB"),
    path('deleteB/<int:id>/',views.deleteBlog, name = "deleteB"),
    path('<int:id>',views.newsDetail, name = "newsDetail"),  
    path('blog',views.blogIndex, name = "blogIndex"),
    path('blog/<int:id>',views.blogDetail, name = "blogDetail"), 
    path('contact', views.contact_us, name='contact_us'),
    path('comment/<int:id>',views.addComment,name = "comment"),
    path('blog/comment/<int:id>', views.addCommentBlog, name="commentBlog"),
    path('adminz/', views.admin_page, name = 'admin_page'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 