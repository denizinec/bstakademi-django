from members.models import Profile
from members.forms import ProfileForm 
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'Kullanıcı bulunamadı.')
            return redirect('/auth/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Hesabınız doğrulanamadı. Lütfen epostanızı kontrol edin.')
            return redirect('/auth/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Yanlış şifre.')
            return redirect('/auth/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'members/login.html')

def logout_user(request):

    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Başarıyla çıkış yapıldı')

    return redirect('/auth/login')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Kullanıcı adı daha önceden alınmış.')
                return redirect('/auth/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Eposta adresi daha önceden alınmış.')
                return redirect('/auth/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/auth/token')

        except Exception as e:
            print(e)


    return render(request , 'members/register.html')

def success(request):
    return render(request , 'members/success.html')

def token_send(request):
    return render(request , 'members/token_send.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Hesabınız zaten doğrulandı.')
                return redirect('/auth/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Hesabınız doğrulandı. Giriş yapabilirsiniz.')
            return redirect('/auth/login')
        else:
            return redirect('/auth/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'members/error.html')

def send_mail_after_registration(email , token):
    subject = 'Hesabınızın doğrulanmış olması gerekiyor. '
    message = f' Adres çubuğuna bu linki yapıştırarak hesabınızı doğrulayabilirsiniz. \n http://127.0.0.1:8000/auth/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


def profileIndex(request, id):
    profileitem = get_object_or_404(Profile, id=id)
    
    profileitemform = ProfileForm(request.POST or None,request.FILES or None, instance=profileitem)

    if profileitemform.is_valid():
        profileitem = profileitemform.save(commit=False)
        profileitem.user = request.user
        profileitem.save()
        return redirect("/polls/")
       
    context = {
        'profileitem':profileitem,
        'profileitemform':profileitemform,
     }
    return render(request, 'members/profile.html', context)