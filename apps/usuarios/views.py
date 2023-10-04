from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome=form['username'].value()
            senha=form['password'].value()

        usuario = auth.authenticate(request, username=nome, password=senha)
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, f'Erro ao efetuar login. Tente novamente.')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            
            
            nome=form['username'].value()
            email=form['email'].value()
            senha=form['password'].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já cadastrado.')
                return redirect('cadastro')

            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return redirect('login')
        
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request): 
    auth.logout(request)
    messages.success(request, 'Usuário deslogado com sucesso.')
    return redirect('login')