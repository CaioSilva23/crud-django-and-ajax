from django.shortcuts import render
from clientes.forms import FormCliente
from clientes.models import Cliente
from django.http import JsonResponse



def home(request):
    form = FormCliente()
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'form': form, 'clientes': clientes})

def save(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # telefone = form.cleaned_data['telefone']
            # cliente = Cliente(nome=nome, email=email, telefone=telefone)
            # cliente.save()
            clientes = Cliente.objects.values()
            clientes_data = list(clientes)
            return JsonResponse({'status': 1, 'clientes_data': clientes_data})
        else:
            return JsonResponse({'status': 0})
        


def delete(request):
    if request.method == 'POST':
        id = request.POST.get('cliente_id')
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})
    

def edit(request):
    if request.method == 'POST':
        id = request.POST.get('cliente_id')
        cliente = Cliente.objects.get(pk=id)
        data = {"id": cliente.id, 
                "nome": cliente.nome, 
                "email": cliente.email, 
                "telefone": cliente.telefone}
        print(data)
        return JsonResponse(data)

