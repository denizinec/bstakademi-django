from django.contrib import admin
from .models import New, Blog, Comment, CommentBlog

admin.site.register(Comment)
admin.site.register(CommentBlog)



@admin.register(New)    # bu işlem direkt admin.register."" seklinde de yapilabilirdi.
class NewAdmin(admin.ModelAdmin):   
    
    list_display = ["id","title","author","created_date",'IsApproved1', 'IsDenied1']

    list_display_links = ["id","title","created_date"]

    search_fields = ["title","content"]

    list_filter = ["created_date"]

    list_editable = ()

    list_per_page = 20

    class Meta: #class içinde meta seklinde class olusturabilme django'da mümkün
        model = New




@admin.register(Blog)    # bu işlem direkt admin.register."" seklinde de yapilabilirdi.
class BlogAdmin(admin.ModelAdmin):   
    
    list_display = ["id","title","author","created_date",'IsApproved2', 'IsDenied2']

    list_display_links = ["id","title","created_date"]

    search_fields = ["title","content"]

    list_filter = ["created_date"]

    list_editable = ()

    list_per_page = 20

    class Meta: #class içinde meta seklinde class olusturabilme django'da mümkün
        model = Blog