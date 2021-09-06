import os
import time
from funcoes import formata_tamanho
# from socket_server.funcoes import formata_tamanho

def calcula_tamanho_pasta(diretorio):
    tamanho = 0

    try:
        for pasta in os.scandir(diretorio):
            if pasta.is_file():
                tamanho += os.stat(pasta).st_size
            else:
                tamanho += calcula_tamanho_pasta(pasta)
    except FileNotFoundError:
        pass
    except NotADirectoryError:
        return os.path.getsize(diretorio)
    except PermissionError:
        return 0

    return tamanho


def busca_arquivo(arquivo,caminho_diretorio,tamanho):

    try:
        for item in os.listdir(caminho_diretorio):
            print(item,os.stat(item).st_size)
            if os.path.isfile(os.path.join(caminho_diretorio, item)):
                if item == arquivo:
                    tamanho += os.stat(item).st_size
            elif os.path.isdir(os.path.join(caminho_diretorio, item)):
                tamanho += busca_arquivo(os.path.join(caminho_diretorio, item), tamanho)
    except FileNotFoundError:
        print("arquivo não encontrado", caminho_diretorio,arquivo)
        pass
    except NotADirectoryError:
        return os.path.getsize(os.path.join(caminho_diretorio,item))
    except PermissionError:
        print("PermissionError")
        return 0
    
    return tamanho

def retorna_arquivos(caminho):
    diretorio = {}  # cria dicionário

    # caminho = r"d:\Users\Matheus\Documents\3 - Acadêmico\OneDrive - al.infnet.edu.br\1 - INFNET\7 - Desenvolvimento Java\1 - Fundamentos do Desenvolvimento Java\Aulas"
    arquivos = os.listdir(caminho)

    # Obtém lista de arquivos e diretórios do diretório corrente:

    for i in arquivos:  # Varia na lista dos arquivos e diretórios
        try:
            idx = arquivos.index(i)
            diretorio[idx] = {}
            nome = os.path.splitext(i)
            diretorio[idx]["nome"] = nome[0]
            diretorio[idx]["tipo"] = nome[1][1:] if nome[1] != '' else 'diretorio'
            diretorio[idx]["tamanho"] = formata_tamanho(busca_arquivo(i,caminho,0))
            diretorio[idx]["dt_criacao"] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(os.stat(i).st_atime))
            diretorio[idx]["dt_modificacao"] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(os.stat(i).st_mtime))
        except Exception:
            continue

    return diretorio