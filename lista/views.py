from django.shortcuts import get_object_or_404, render, redirect
from lista.forms import ListaForms
from .models import Lista

def index(request):
    listas = Lista.objects.all().order_by('id')
    dados = {
        'listas' : listas
    }
    return render(request, 'index.html', dados)


def novo_item(request):
    form = ListaForms(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'add_item.html', {'form': form})

def edit_item(request, id):
    item = get_object_or_404(Lista, pk=id)
    form = ListaForms(instance=item)

    if request.method == 'POST':
        form = ListaForms(request.POST, instance=item)

        if(form.is_valid()):
            form.save()
            return redirect('index')
        else:
            return render(request, 'update_item.html', {'form': form, 'item': item})
    else:
        return render(request, 'update_item.html', {'form': form, 'item': item})
    
def delete_item(request, id):
    item = get_object_or_404(Lista, pk=id)
    item.delete()
    return redirect('index')
    