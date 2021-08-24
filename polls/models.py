from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

User = "auth.User"

class ProjectIdea(models.Model):
    projectAuthor = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName = models.CharField(max_length=100, verbose_name='ad')
    projectSurname = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied = models.BooleanField(default= False, verbose_name='Red')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName


class Comment(models.Model):
    post = models.ForeignKey(ProjectIdea, on_delete = models.CASCADE, related_name="comments")
    name =  models.ForeignKey(User,on_delete = models.CASCADE, related_name="names")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName} - {self.name}'



class week1(models.Model):
    projectAuthor1 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName1 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname1 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber1 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName1 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription1 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved1 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied1 = models.BooleanField(default= False, verbose_name='Red')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName1


class Comment1(models.Model):
    post = models.ForeignKey(week1, on_delete = models.CASCADE, related_name="comments1")
    name =  models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName1} - {self.name}'



class Week2(models.Model):
    projectAuthor2 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName2 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname2 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber2 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName2 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription2 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved2 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied2 = models.BooleanField(default= False, verbose_name='Red')
    created_date2 = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName2

class Comment2(models.Model):
    post = models.ForeignKey(Week2, on_delete = models.CASCADE, related_name="comments2")
    name =  models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName2} - {self.name}'


class Week3(models.Model):
    projectAuthor3 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName3 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname3 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber3 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName3 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription3 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved3 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied3 = models.BooleanField(default= False, verbose_name='Red')
    created_date3 = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName3

class Comment3(models.Model):
    post = models.ForeignKey(Week3, on_delete = models.CASCADE, related_name="comments3")
    name =  models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName3} - {self.name}'



class Week4(models.Model):
    projectAuthor4 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName4 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname4 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber4 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName4 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription4 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved4 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied4 = models.BooleanField(default= False, verbose_name='Red')
    created_date4 = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName4

class Comment4(models.Model):
    post = models.ForeignKey(Week4, on_delete = models.CASCADE, related_name="comments4")
    name =  models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName4} - {self.name}'


class Week5(models.Model):
    projectAuthor5 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName5 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname5 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber5 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName5 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription5 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved5 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied5 = models.BooleanField(default= False, verbose_name='Red')
    created_date5 = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName5

class Comment5(models.Model):
    post = models.ForeignKey(Week5, on_delete = models.CASCADE, related_name="comments5")
    name =  models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName5} - {self.name}'


class Week6(models.Model):
    projectAuthor6 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName6 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname6 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber6 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName6 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription6 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved6 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied6 = models.BooleanField(default= False, verbose_name='Red')
    created_date6 = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName6

class Comment6(models.Model):
    post = models.ForeignKey(Week6, on_delete = models.CASCADE, related_name="comments6")
    name =  models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName6} - {self.name}'


class Week7(models.Model):
    projectAuthor7 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName7 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname7 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber7 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName7 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription7 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved7 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied7 = models.BooleanField(default= False, verbose_name='Red')
    created_date7 = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName7


class Comment7(models.Model):
    post = models.ForeignKey(Week7, on_delete = models.CASCADE, related_name="comments7")
    name =  models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName7} - {self.name}'


class Week8(models.Model):
    projectAuthor8 = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name="Kullanıcı Adı")
    projectName8 = models.CharField(max_length=100, verbose_name='ad')
    projectSurname8 = models.CharField(max_length=100, verbose_name='soy ad')
    projectNumber8 = models.IntegerField(max_length=10, verbose_name='okul no')
    projectPName8 = models.CharField(max_length=100, verbose_name='Proje Adı')
    projectDescription8 = RichTextField(blank=True, null=True, verbose_name='Proje Açıklama')
    projectIsApproved8 = models.BooleanField(default= False, verbose_name='Onay')
    projectIsDenied8 = models.BooleanField(default= False, verbose_name='Red')
    created_date8 = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    

    def __str__(self):
        return self.projectName8

class Comment8(models.Model):
    post = models.ForeignKey(Week8, on_delete = models.CASCADE, related_name="comments8")
    name =  models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.projectName8} - {self.name}'