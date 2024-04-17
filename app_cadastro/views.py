from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # Corrigido o redirecionamento
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/criar_usuario.html', {'form': form})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def atualiza_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # Corrigido o redirecionamento
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/atualiza_usuario.html', {'form': form})

def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/deletar_usuario.html', {'usuario': usuario})

def home(request):
    return render(request, 'usuarios/home.html')

def pesquisar_usuarios(request):
    if 'q' in request.GET:
        query = request.GET['q']
        usuarios = Usuario.objects.filter(nome__icontains=query)
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'usuarios/pesquisar_usuarios.html', {'usuarios': usuarios}),

def salvar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/criar_usuario.html', {'form': form})