from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

User = "auth.User"

class New(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 144,verbose_name = "Başlık")
    content = RichTextField(verbose_name= "İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    news_image = models.ImageField(blank = True,null = True,verbose_name="Fotoğraf Ekleyin")
    post_views = models.IntegerField(default=0, null=True, blank=True)
    IsApproved1 = models.BooleanField(default= False, verbose_name='Onay')
    IsDenied1 = models.BooleanField(default= False, verbose_name='Red')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 144,verbose_name = "Başlık")
    content = RichTextField(verbose_name= "İçerik")
    summary = models.TextField(verbose_name="Özet")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    news_image = models.ImageField(blank = True,null = True,verbose_name="Fotoğraf Ekleyin")
    post_views = models.IntegerField(default=0, null=True, blank=True)
    isPublished = models.BooleanField(default=False)
    IsApproved2 = models.BooleanField(default= False, verbose_name='Onay')
    IsDenied2 = models.BooleanField(default= False, verbose_name='Red')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    news = models.ForeignKey(New,on_delete = models.CASCADE, verbose_name = "Haber Başlığı",related_name="comments")
    comment_author = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_content = RichTextField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']


class CommentBlog(models.Model):
    blogs = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name= "Blog Başlığı", related_name="commentz")
    comment_author = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_content = RichTextField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

