from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from members.models import Profile

@login_required(login_url='')
def pollsIndex(request):
    projectIdeaPost = ProjectIdea.objects.filter(projectAuthor=request.user)
    projectIdeaPostControl = ProjectIdea.objects.filter(projectAuthor=request.user, projectIsApproved=True)

    profilePost =  Profile.objects.filter(user=request.user)[0:1]

    week1Post = week1.objects.filter(projectAuthor1=request.user)
    week2Post = Week2.objects.filter(projectAuthor2=request.user)
    week3Post = Week3.objects.filter(projectAuthor3=request.user)
    week4Post = Week4.objects.filter(projectAuthor4=request.user)
    week5Post = Week5.objects.filter(projectAuthor5=request.user)
    week6Post = Week6.objects.filter(projectAuthor6=request.user)
    week7Post = Week7.objects.filter(projectAuthor7=request.user)
    week8Post = Week8.objects.filter(projectAuthor8=request.user)
    
    projectideaform = ProjectIdeaForm()
    week1form = week1Form()
    week2form = week2Form()
    week3form = week3Form()
    week4form = week4Form()
    week5form = week5Form()
    week6form = week6Form()
    week7form = week7Form()
    week8form = week8Form()

    if request.method == 'POST':

        projectideaform = ProjectIdeaForm(request.POST)
        if projectideaform.is_valid():
            instance = projectideaform.save(commit=False)
            instance.projectAuthor = request.user

        week1form = week1Form(request.POST)
        if week1form.is_valid():
            instance = week1form.save(commit=False)
            instance.projectAuthor1 = request.user

        week2form = week2Form(request.POST)
        if week2form.is_valid():
            instance = week2form.save(commit=False)
            instance.projectAuthor2 = request.user
    
        week3form = week3Form(request.POST)
        if week3form.is_valid():
            instance = week3form.save(commit=False)
            instance.projectAuthor3 = request.user

        week4form = week4Form(request.POST)
        if week4form.is_valid():
            instance = week4form.save(commit=False)
            instance.projectAuthor4 = request.user

        week5form = week5Form(request.POST)
        if week5form.is_valid():
            instance = week5form.save(commit=False)
            instance.projectAuthor5 = request.user

        week6form = week6Form(request.POST)
        if week6form.is_valid():
            instance = week6form.save(commit=False)
            instance.projectAuthor6 = request.user
 
        week7form = week7Form(request.POST)
        if week7form.is_valid():
            instance = week7form.save(commit=False)
            instance.projectAuthor7 = request.user

        week8form = week8Form(request.POST)
        if week8form.is_valid():
            instance = week8form.save(commit=False)
            instance.projectAuthor8 = request.user
            
        instance.save()
        return redirect('/polls/')
       
    context = {
        'projectIdeaPost':projectIdeaPost,
        'projectIdeaPostControl':projectIdeaPostControl,
        'projectideaform':projectideaform,

        'week1Post':week1Post,
        'week1form':week1Form,

        'week2Post':week2Post,
        'week2form':week2form,

        'week3Post':week3Post,
        'week3form':week3form,

        'week4Post':week4Post,
        'week4form':week4form,

        'week5Post':week5Post,
        'week5form':week5form,

        'week6Post':week6Post,
        'week6form':week6form,

        'week7Post':week7Post,
        'week7form':week7form,

        'week8Post':week8Post,
        'week8form':week8form,

        'profilePost':profilePost,
    }
    
    return render(request, 'polls/polls.html', context)


@login_required
def pollsDelete0(request, pk):
    projectIdeaPost = get_object_or_404(ProjectIdea, id=pk) #.filter(projectAuthor=request.user)
    projectIdeaPost.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete(request, pk):
    week1Post = get_object_or_404(week1, id=pk)
    week1Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete2(request, pk):
    week2Post = get_object_or_404(Week2, id=pk)
    week2Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete3(request, pk):
    week3Post = get_object_or_404(Week3, id=pk)
    week3Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete4(request, pk):
    week4Post = get_object_or_404(Week4, id=pk)
    week4Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete5(request, pk):
    week5Post = get_object_or_404(Week5, id=pk)
    week5Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete6(request, pk):
    week6Post = get_object_or_404(Week6, id=pk)
    week6Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete7(request, pk):
    week7Post = get_object_or_404(Week7, id=pk)
    week7Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDelete8(request, pk):
    week8Post = get_object_or_404(Week8, id=pk)
    week8Post.delete()
    return redirect('pollsIndex')

@login_required(login_url='')
def pollsDetail0(request, pk):

    projectIdeaDetailPost = get_object_or_404(ProjectIdea, id=pk)
    projectideaform1 = ProjectIdeaForm1(instance=projectIdeaDetailPost)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = projectIdeaDetailPost
            obj.save()

            return redirect('pollsDetail0', pk=projectIdeaDetailPost.pk)    

    else:
        form = CommentForm()


    if request.method == 'POST':
        projectideaform1 = ProjectIdeaForm1(request.POST, instance=projectIdeaDetailPost)
        if projectideaform1.is_valid():
            projectideaform1.save()
            return redirect('pollsDetail0', pk=projectIdeaDetailPost.pk)

    context = {
        'projectIdeaDetailPost':projectIdeaDetailPost,
        'projectideaform1':projectideaform1,   
        'form':form,  
    }
    
    return render(request, 'polls/pollsdetail.html', context)


@login_required(login_url='')
def pollsDetail(request, pk):

    week1DetailPost = week1.objects.get(id=pk)
    week1form1 = week1Form1(instance=week1DetailPost)

    if request.method == 'POST':
        form = CommentForm1(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week1DetailPost
            obj.save()

            return redirect('pollsDetail', pk=week1DetailPost.pk)    

    else:
        form = CommentForm1()

    if request.method == 'POST':
        week1form1 = week1Form1(request.POST, instance=week1DetailPost)
        if week1form1.is_valid():
            week1form1.save()
            return redirect('pollsDetail', pk=week1DetailPost.pk)    
    
    context = {
        'week1DetailPost':week1DetailPost,
        'week1form1':week1form1,
        'form':form,     
    }
    
    return render(request, 'polls/pollsdetail.html', context)

@login_required(login_url='')
def pollsDetail2(request, pk):

    week2DetailPost = Week2.objects.get(id=pk)
    week2form2 = week2Form2(instance=week2DetailPost)

    if request.method == 'POST':
        form = CommentForm2(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week2DetailPost
            obj.save()

            return redirect('pollsDetail2', pk=week2DetailPost.pk)    

    else:
        form = CommentForm2()

    if request.method == 'POST':
        week2form2 = week2Form2(request.POST, instance=week2DetailPost)
        if week2form2.is_valid():
            week2form2.save()
            return redirect('pollsDetail2', pk=week2DetailPost.pk)

    context = {
        'week2DetailPost':week2DetailPost,
        'week2form2':week2form2,
        'form':form,   
    }
    
    return render(request, 'polls/pollsdetail.html', context)

@login_required(login_url='')
def pollsDetail3(request, pk):

    week3DetailPost = Week3.objects.get(id=pk)
    week3form3 = week3Form3(instance=week3DetailPost)

    if request.method == 'POST':
        form = CommentForm3(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week3DetailPost
            obj.save()

            return redirect('pollsDetail3', pk=week3DetailPost.pk)
    else:
        form = CommentForm3()

    if request.method == 'POST':
        week3form3 = week3Form3(request.POST, instance=week3DetailPost)
        if week3form3.is_valid():
            week3form3.save()
            return redirect('pollsDetail3', pk=week3DetailPost.pk)

    context = {
        'week3DetailPost':week3DetailPost,
        'week3form3':week3form3,
        'form':form,
    }
    
    return render(request, 'polls/pollsdetail.html', context)

@login_required(login_url='')
def pollsDetail4(request, pk):

    week4DetailPost = Week4.objects.get(id=pk)
    week4form4 = week4Form4(instance=week4DetailPost)

    if request.method == 'POST':
        form = CommentForm4(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week4DetailPost
            obj.save()

            return redirect('pollsDetail4', pk=week4DetailPost.pk)
    else:
        form = CommentForm4()

    if request.method == 'POST':
        week4form4 = week4Form4(request.POST, instance=week4DetailPost)
        if week4form4.is_valid():
            week4form4.save()
            return redirect('pollsDetail4', pk=week4DetailPost.pk)
   
    context = {
        'week4DetailPost':week4DetailPost,
        'week4form4':week4form4,
        'form':form,
    }
    
    return render(request, 'polls/pollsdetail.html', context)

@login_required(login_url='')
def pollsDetail5(request, pk):

    week5DetailPost = Week5.objects.get(id=pk)
    week5form5 = week5Form5(instance=week5DetailPost)

    if request.method == 'POST':
        form = CommentForm5(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week5DetailPost
            obj.save()

            return redirect('pollsDetail5', pk=week5DetailPost.pk)
    else:
        form = CommentForm5()

    if request.method == 'POST':
        week5form5 = week5Form5(request.POST, instance=week5DetailPost)
        if week5form5.is_valid():
            week5form5.save()
            return redirect('pollsDetail5', pk=week5DetailPost.pk)
   
    context = {
        'week5DetailPost':week5DetailPost,
        'week5form5':week5form5,
        'form':form,
    }
    
    return render(request, 'polls/pollsdetail.html', context)

@login_required(login_url='')
def pollsDetail6(request, pk):

    week6DetailPost = Week6.objects.get(id=pk)
    week6form6 = week6Form6(instance=week6DetailPost)

    if request.method == 'POST':
        form = CommentForm6(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week6DetailPost
            obj.save()

            return redirect('pollsDetail6', pk=week6DetailPost.pk)
    else:
        form = CommentForm6()
    
    if request.method == 'POST':
        week6form6 = week6Form6(request.POST, instance=week6DetailPost)
        if week6form6.is_valid():
            week6form6.save()
            return redirect('pollsDetail6', pk=week6DetailPost.pk)

    context = {
        'week6DetailPost':week6DetailPost,
        'week6form6':week6form6,
        'form':form,
    }
    
    return render(request, 'polls/pollsdetail.html', context)

@login_required(login_url='')
def pollsDetail7(request, pk):

    week7DetailPost = Week7.objects.get(id=pk)
    week7form7 = week7Form7(instance=week7DetailPost)

    if request.method == 'POST':
        form = CommentForm7(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week7DetailPost
            obj.save()

            return redirect('pollsDetail7', pk=week7DetailPost.pk)
    else:
        form = CommentForm7()
    

    if request.method == 'POST':
        week7form7 = week7Form7(request.POST, instance=week7DetailPost)
        if week7form7.is_valid():
            week7form7.save()
            return redirect('pollsDetail7', pk=week7DetailPost.pk)

    context = {
        'week7DetailPost':week7DetailPost,
        'week7form7':week7form7,
        'form':form,
    }
    
    return render(request, 'polls/pollsdetail.html', context)

@login_required(login_url='')
def pollsDetail8(request, pk):

    week8DetailPost = Week8.objects.get(id=pk)
    week8form8 = week8Form8(instance=week8DetailPost)

    if request.method == 'POST':
        form = CommentForm8(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.post = week8DetailPost
            obj.save()

            return redirect('pollsDetail8', pk=week8DetailPost.pk)
    else:
        form = CommentForm8()
    

    if request.method == 'POST':
        week8form8 = week8Form8(request.POST, instance=week8DetailPost)
        if week8form8.is_valid():
            week8form8.save()
            return redirect('pollsDetail8', pk=week8DetailPost.pk)


    context = {
        'week8DetailPost':week8DetailPost,
        'week8form8':week8form8,
        'form':form,
    }
    
    return render(request, 'polls/pollsdetail.html', context)