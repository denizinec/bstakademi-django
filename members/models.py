from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name = "Ad")
    surname = models.CharField(max_length=100,  null=True, blank=True, verbose_name = "Soyad")
    email = models.CharField(max_length = 80,  null=True, blank=True, verbose_name = "Email")
    bio = models.CharField(max_length = 80,  null=True, blank=True, verbose_name = "Biyografi")
    skills = models.CharField(max_length = 80,  null=True, blank=True, verbose_name = "Yetenekler")
    phone_n = models.IntegerField(max_length = 11,  null=True, blank=True, verbose_name = "Telefon")
    school_n = models.IntegerField(max_length = 11,  null=True, blank=True, verbose_name = "Okul No")
    school = models.CharField(max_length=100,  null=True, blank=True, verbose_name= "Okul / Bölüm")
    profile_pic = models.ImageField(blank = True,null = True,verbose_name="Kullanıcı Fotoğrafı")

    def __str__(self):
        return self.user.username