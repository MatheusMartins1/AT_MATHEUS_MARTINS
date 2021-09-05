import os
import time
from funcoes import formata_tamanho

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

# caminho = r"D:\Users\Matheus\Documents\workspacePython"
def retorna_arquivos(caminho):
    diretorio = {}  # cria dicionário
    # diretorio = {"arquivos":caminho}
    arquivos = os.listdir(caminho)

    # Obtém lista de arquivos e diretórios do diretório corrente:

    for i in arquivos:  # Varia na lista dos arquivos e diretórios
        try:
            idx = arquivos.index(i)
            diretorio[idx] = {}
            nome = os.path.splitext(i)
            diretorio[idx]["nome"] = nome[0]
            diretorio[idx]["tipo"] = nome[1][1:] if nome[1] != '' else 'diretorio'
            diretorio[idx]["tamanho"] = formata_tamanho(calcula_tamanho_pasta(i))
            diretorio[idx]["dt_criacao"] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(os.stat(i).st_atime))
            diretorio[idx]["dt_modificacao"] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(os.stat(i).st_mtime))
        except Exception:
            continue

    return diretorio