from django.contrib import admin
from .models import *


class pollsAdmin0(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor', 'projectNumber','created_date', 'projectIsApproved', 'projectIsDenied')
    list_display_links = ('id', 'projectAuthor')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date',)
    list_editable = ()
    search_fields = ('projectAuthor', 'projectDescription', 'projectNumber')
    list_per_page = 20

class CommentAdmin0(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'post', 'name','date_added')
    list_display_links = ('id', 'post')#id ve name ler link olarak gözükecektir
    list_filter = ('date_added',)
    list_editable = ()
    search_fields = ('name', 'post', 'date_added')
    list_per_page = 20

class pollsAdmin(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor1', 'projectNumber1','created_date', 'projectIsApproved1', 'projectIsDenied1')
    list_display_links = ('id', 'projectAuthor1')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date',)
    list_editable = ()
    search_fields = ('projectAuthor1', 'projectDescription1', 'projectNumber1')
    list_per_page = 20


class pollsAdmin2(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor2', 'projectNumber2','created_date2', 'projectIsApproved2', 'projectIsDenied2')
    list_display_links = ('id', 'projectAuthor2')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date2',)
    list_editable = ()
    search_fields = ('projectAuthor2', 'projectDescription2', 'projectNumber2')
    list_per_page = 20


class pollsAdmin3(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor3', 'projectNumber3','created_date3', 'projectIsApproved3', 'projectIsDenied3')
    list_display_links = ('id', 'projectAuthor3')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date3',)
    list_editable = ()
    search_fields = ('projectAuthor3', 'projectDescription3', 'projectNumber3')
    list_per_page = 20


class pollsAdmin4(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor4', 'projectNumber4','created_date4', 'projectIsApproved4', 'projectIsDenied4')
    list_display_links = ('id', 'projectAuthor4')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date4',)
    list_editable = ()
    search_fields = ('projectAuthor4', 'projectDescription4', 'projectNumber4')
    list_per_page = 20

class pollsAdmin5(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor5', 'projectNumber5','created_date5', 'projectIsApproved5', 'projectIsDenied5')
    list_display_links = ('id', 'projectAuthor5')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date5',)
    list_editable = ()
    search_fields = ('projectAuthor5', 'projectDescription5', 'projectNumber5')
    list_per_page = 20

class pollsAdmin6(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor6', 'projectNumber6','created_date6', 'projectIsApproved6', 'projectIsDenied6')
    list_display_links = ('id', 'projectAuthor6')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date6',)
    list_editable = ()
    search_fields = ('projectAuthor6', 'projectDescription6', 'projectNumber6')
    list_per_page = 20

class pollsAdmin7(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor7', 'projectNumber7','created_date7', 'projectIsApproved7', 'projectIsDenied7')
    list_display_links = ('id', 'projectAuthor7')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date7',)
    list_editable = ()
    search_fields = ('projectAuthor7', 'projectDescription7', 'projectNumber7')
    list_per_page = 20

class pollsAdmin8(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'projectAuthor8', 'projectNumber8','created_date8', 'projectIsApproved8', 'projectIsDenied8')
    list_display_links = ('id', 'projectAuthor8')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date8',)
    list_editable = ()
    search_fields = ('projectAuthor8', 'projectDescription8', 'projectNumber8')
    list_per_page = 20
# Register your models here.

admin.site.register(ProjectIdea, pollsAdmin0)

admin.site.register(week1, pollsAdmin)

admin.site.register(Week2, pollsAdmin2)

admin.site.register(Week3, pollsAdmin3)

admin.site.register(Week4, pollsAdmin4)

admin.site.register(Week5, pollsAdmin5)

admin.site.register(Week6, pollsAdmin6)

admin.site.register(Week7, pollsAdmin7)

admin.site.register(Week8, pollsAdmin8)


admin.site.register(Comment, CommentAdmin0)
admin.site.register(Comment1, CommentAdmin0)
admin.site.register(Comment2, CommentAdmin0)
admin.site.register(Comment3, CommentAdmin0)
admin.site.register(Comment4, CommentAdmin0)
admin.site.register(Comment5, CommentAdmin0)
admin.site.register(Comment6, CommentAdmin0)
admin.site.register(Comment7, CommentAdmin0)
admin.site.register(Comment8, CommentAdmin0)