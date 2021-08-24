from django.shortcuts import render
from app.models import New, Blog, Comment, CommentBlog
from app.views import CreateNewForm
from polls.views import pollsIndex
from polls.models import ProjectIdea


def user_proifle(request):   
    p = ProjectIdea.objects.all
    return render(request, 'partials/user.html')


