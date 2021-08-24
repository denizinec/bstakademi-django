from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


User = "auth.User"

class Contact(models.Model):
    name = models.CharField(max_length=100,  verbose_name = "Ad")
    surname = models.CharField(max_length=100,   verbose_name = "Soyad")
    email = models.CharField(max_length = 80,   verbose_name = "Email")
    subject = models.CharField(max_length = 80,  verbose_name = "Konu")
    phone_n = models.IntegerField(max_length = 11,  verbose_name = "Telefon")
    message = models.CharField(max_length= 288, verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tarih")

    def __str__(self):
        return self.email


