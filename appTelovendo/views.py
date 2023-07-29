from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def colaboracion(request):
    return render(request,'colaboracion.html')

def crearProveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos se han guardado con éxito.')
            return redirect('app:colaboracion')
    else:
        form = ProveedorForm()
    return render(request, 'crearProveedor.html', { 'form': form })

