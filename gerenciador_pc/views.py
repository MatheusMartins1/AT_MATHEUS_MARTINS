from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from gerenciador_pc.cliente_socket import cliente_socket
from socket_server.funcoes import  pickle_to_dict
from gerenciador_pc.forms import CaminhoPastaForm

def index(request):
    pc = cliente_socket.requisita_servidor_socket("pc")
    PC = pickle_to_dict(pc)
    contexto = PC
    return render(request, 'pc.html', contexto)


def processos(request):
    processos = cliente_socket.requisita_servidor_socket("processos")
    contexto = {"processos": processos}
    return render(request, 'processos.html', contexto)


def arquivos(request):
    contexto = {}
    return render(request, 'arquivos.html', contexto)


def listar_arquivos(request, caminho):
    arquivos = cliente_socket.requisita_servidor_socket(f"arquivos;{caminho}")
    contexto = {"arquivos": arquivos}
    return render(request, 'arquivos.html', contexto)


@csrf_protect
def caminho_pasta(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CaminhoPastaForm(request.POST)
        if form.is_valid():
            caminho_informado = form.clean()['caminho_pasta']

        return listar_arquivos(request, caminho_informado)
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CaminhoPastaForm()

    contexto = {}
    return arquivos(request)


def rede(request):
    rede = cliente_socket.requisita_servidor_socket("rede")
    print(rede)
    contexto = {"rede": rede[0],"interfaces":rede[1]}
    return render(request, 'rede.html', contexto)


def relatorio(request):
    contexto = {}
    return render(request, 'relatorio.html', contexto)