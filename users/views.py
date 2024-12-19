
from email.policy import HTTP
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from django.urls import reverse
from django.shortcuts import render, redirect


from users.models import User

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
            
    context = {
        'title':'GreedGaming - Авторазция',
        'form':form
    }
    return render(request, 'users/login.html', context)

def registration(request):
        if request.method == 'POST':
            form = UserRegistrationForm(data=request.POST)
            if form.is_valid():
                form.save()
                user = form.instance
                auth.login(request, user)
                messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
                return HttpResponseRedirect(reverse('main:index'))          
        else:
            form = UserRegistrationForm()

        context = {
            'title':'GreedGaming - Регистрация',
            'form': form
    }
        return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('users:profile'))          
    else:
        form = ProfileForm(instance=request.user)

        context = {
            'title':'GreedGaming - Кабинет',
            'form': form
        }
        return render(request, 'users/profile.html', context)
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы успешно вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))




# Create your views here.