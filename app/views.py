from members.models import Profile
from polls.models import ProjectIdea
from django.db.models.fields import CharField
from .forms import CreateNewForm, CreateBlogForm, BlogFormApprov
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import Http404
from .models import *
from polls.models import *
from django.db.models import Count
from django.contrib.auth.models import User



def newsIndex(request):   
    newsPosts1 = New.objects.filter().order_by('-created_date')[0:1]
    newsPosts2 = New.objects.filter().order_by('-created_date')[1:3]
    newsPosts3 = New.objects.all().order_by('-created_date')[3::]
    blogPostNews = Blog.objects.filter(IsApproved2 = True).order_by('-created_date')[0:4]

    blogPostMostViews = Blog.objects.filter(IsApproved2 = True).order_by('-post_views', '-created_date')[0:3]

    

    context = {
        'newsPosts1': newsPosts1,
        'newsPosts2': newsPosts2,
        'newsPosts3': newsPosts3,
        'blogPostNews': blogPostNews,

        'blogPostMostViews':blogPostMostViews,
        }

    return render(request, 'news/news.html', context)

def createNew(request):    
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("/auth/login")

    form = CreateNewForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = CreateNewForm()
        return redirect("/dnew")

    context['form'] = form

    return render(request, "news/add_new.html", context)

def newsDetail(request,id):    
    newsPostDetail = get_object_or_404(New,id = id) 
    newsPostDetail.post_views = newsPostDetail.post_views + 1
    newsPostDetail.save()
    comments = newsPostDetail.comments.all()
    newsPosts4 = New.objects.filter().order_by('-created_date')[0:5]#populer post için 
    newsDetailBlogPost = Blog.objects.filter().order_by('-created_date')[0:2]#news detailda ki son blog haberleri
    

    context = {
        'newsPostDetail': newsPostDetail,
        'newsPosts4': newsPosts4,  
        'newsDetailBlogPost': newsDetailBlogPost,
        'comments':comments,
    }

    return render(request,"news/newsdetail.html", context)

def updateNew(request,id):
    new = get_object_or_404(New,id = id)
    form = CreateNewForm(request.POST or None,request.FILES or None, instance=new)
    
    if form.is_valid():
        new = form.save(commit=False)
        new.author = request.user
        new.save()
        return redirect("/dnew")

    context = {'form':form}
    return render(request,"news/update_new.html", context)

def ndashboard(request):   
    newsPosts1 = New.objects.filter(author = request.user).order_by('-created_date')

    profilePost =  Profile.objects.filter(user=request.user)[0:1]

    context = {
        'newsPosts1': newsPosts1, 
        'profilePost':profilePost,       
        }

    

    return render(request,"news/dashboard.html",context)

def deleteNew(request,id):
    new = get_object_or_404(New,id = id)
    new.delete()    
    return redirect("/dnew")

def blogIndex(request):   
    blogsPost = Blog.objects.all().order_by('-created_date').filter(IsApproved2=True)

    newsPostMostViews = New.objects.filter().order_by('-post_views', '-created_date')[0:3]
    newsPostRecentPost = New.objects.filter().order_by('-created_date')[0:3]
    
    context = {
        'blogsPost': blogsPost,
        'newsPostMostViews':newsPostMostViews,
        'newsPostRecentPost':newsPostRecentPost,
    }
    
    return render(request, 'blog/blog.html', context)

def createBlog(request):    

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("/auth/login")
        
    form = CreateBlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = CreateNewForm()
        return redirect("/dblog")

    context['form'] = form

    return render(request, "blog/add_blog.html", context)

def blogDetail(request,id):    
    

    if request.user.is_superuser:
        blogPostDetail = get_object_or_404(Blog, id = id)
    elif not request.user.is_superuser:
        blogPostDetail = get_object_or_404(Blog, id = id, IsApproved2 = True)

    blogPostDetail.post_views = blogPostDetail.post_views + 1
    blogPostDetail.save()
    commentz = blogPostDetail.commentz.all()

    blogFormApprov = BlogFormApprov(instance=blogPostDetail)

    if request.method == 'POST':
        blogFormApprov = BlogFormApprov(request.POST, instance=blogPostDetail)
        if blogFormApprov.is_valid():
            blogFormApprov.save()
            return redirect('blogDetail', id=blogPostDetail.id)



    context = {
        'blogPostDetail': blogPostDetail,  
        'commentz':commentz,
    }

    return render(request,"blog/blogdetail.html", context)

def bdashboard(request):   
    blogsPost = Blog.objects.filter(author = request.user).order_by('-created_date') 

    profilePost =  Profile.objects.filter(user=request.user)[0:1]   
    
    context = {
        'blogsPost': blogsPost,
        "sayfagirdisi":5,
        'profilePost':profilePost,
        }

    return render(request,"blog/dashboard.html",context)

def updateBlog(request,id):
    blog = get_object_or_404(Blog,id = id)
    form = CreateBlogForm(request.POST or None,request.FILES or None, instance=blog)
    
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect("/dblog")

    context = {'form':form}
    return render(request,"blog/update_blog.html", context)

def deleteBlog(request,id):
    blog = get_object_or_404(Blog,id = id)
    blog.delete()    

    return redirect("dblog")

def contact_us(request):
    return render(request,"contact_us/hakkımızda.html")

def addComment(request,id):
    news = get_object_or_404(New, id = id)
    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.news = news

        newComment.save()
    return redirect(reverse("newsDetail",kwargs={"id":id}))

def addCommentBlog(request,id):
    blogs = get_object_or_404(Blog,id=id)
    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")

        newComment = CommentBlog(comment_author  = comment_author, comment_content = comment_content)

        newComment.blogs = blogs

        newComment.save()
    return redirect(reverse("blogDetail",kwargs={"id":id}))



def admin_page(request):
    projefikir = ProjectIdea.objects.all()
    hafta1 = week1.objects.all()
    hafta2 = Week2.objects.all()
    hafta3 = Week3.objects.all()
    hafta4 = Week4.objects.all()
    hafta5 = Week5.objects.all()
    hafta6 = Week6.objects.all()
    hafta7 = Week7.objects.all()
    hafta8 = Week8.objects.all()
    haberler = New.objects.all()
    bloglar = Blog.objects.all()
    context ={
        'projefikir':projefikir,
        'hafta1':hafta1,
        'hafta2':hafta2,
        'hafta3':hafta3,
        'hafta4':hafta4,
        'hafta5':hafta5,
        'hafta6':hafta6,
        'hafta7':hafta7,
        'hafta8':hafta8,
        'haberler':haberler,
        'bloglar':bloglar,
    }
    return render(request, 'members/admin.html',context)