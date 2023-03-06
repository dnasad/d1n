from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout

# Create your views here.
def index(request):
    return render(request, 'webProjectApplication/index.html')


def login(request):
    return render(request, 'webProjectApplication/login.html')


def mcs(request):
    return render(request, 'webProjectApplication/mcs.html')

def reg(request):
    return render(request, 'webProjectApplication/reg.html')

def navmen_podgotovka(request):
    return render(request, 'webProjectApplication/navmen_podgotovka.html')




def reg(request):
    form = UserRegisterForm() 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('success')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'webProjectApplication/reg.html', {"form": form})

def success(request):
    return render(request, 'webProjectApplication/success.html')

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            reg(request, user)
            return redirect ('index')
    else:
        form = UserLoginForm()
    return render(request, 'webProjectApplication/reg.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('reg')




