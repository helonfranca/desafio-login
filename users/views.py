from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import user_passes_test, login_required

def redirecionar_se_logado(user):
    return not user.is_authenticated

@user_passes_test(redirecionar_se_logado, login_url='/menu/')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'menu/menu.html', {'form': form})
        else:
            # Se o formulário não for válido, exibe os erros
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = LoginForm()
    
    return render(request, 'auth/login.html', {'form': form})

@user_passes_test(redirecionar_se_logado, login_url='/menu/')
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registro realizado com sucesso!")
            return render(request, 'auth/register.html', {'form': form})
        else:
            # Se o formulário não for válido, exibe os erros
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = RegisterForm()
    
    return render(request, 'auth/register.html', {'form': form})

@login_required(login_url='/login/')
def menu_view(request):
    return render(request, 'menu/menu.html')