import os
import subprocess
import platform
import psutil
import nmap
from asgiref.sync import sync_to_async
import asyncio

def retorna_codigo_ping(hostname):
    """Usa o utilitario ping do sistema operacional para encontrar   o host. ('-c 5') indica, em sistemas linux, que deve mandar 5   pacotes. ('-W 3') indica, em sistemas linux, que deve esperar 3   milisegundos por uma resposta. Esta funcao retorna o codigo de   resposta do ping """

    plataforma = platform.system()
    args = []
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    ret_cod = subprocess.call(args,
                              stdout=open(os.devnull, 'w'),
                              stderr=open(os.devnull, 'w'))
    return ret_cod

def verifica_hosts(sub_rede):
    """Verifica todos os host com a sub_rede entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
    print("Mapeando\r")

    return_codes = dict()

    for i in range(1, 255):
        ip = sub_rede + '{0}'.format(i)
        return_codes[ip] = retorna_codigo_ping(ip)

        if i % 20 == 0:
            print(".", end="")
        if return_codes[ip] == 0:
            enderecos_ativos[i] = {"ip": ip}

    print("\nMapping ready...")


def scan_host(host,id):

    try:
        nm = nmap.PortScanner()
        nm.scan(host)

        enderecos_ativos[id]["hostname"] = nm[host].hostname()
        enderecos_ativos[id]["portas"] = {}

        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocolo : %s' % proto)

            lport = nm[host][proto].keys()
            # lport.sort()
            for port in lport:
                print(f"escaneando porta {port}")
                enderecos_ativos[id]["portas"][port] = {}
                enderecos_ativos[id]["portas"][port]["porta"] = port
                enderecos_ativos[id]["portas"][port]["estado"] = nm[host][proto][port]['state']
                enderecos_ativos[id]["portas"][port]["protocolo"] = proto
                enderecos_ativos[id]["portas"][port]["product"] = nm[host][proto][port]['product']
    except Exception as e:
        print("erro",e)

enderecos_ativos = {}

def exec_info_redes():
    from datetime import datetime
    from time import sleep
    sleep(1)
    timeStart = datetime.now()
    print("iniciando execução")
    if len(enderecos_ativos) == 0:
        rede = psutil.net_if_addrs()['Ethernet'][1]
        ip_lista = rede.address.split('.')
        sub_rede = ".".join(ip_lista[0:3]) + '.'

        verifica_hosts(sub_rede)

        for endereco in enderecos_ativos:

            print('----------')
            print(f'escaneando {enderecos_ativos[endereco]["ip"]}')

            scan_host(enderecos_ativos[endereco]["ip"],endereco)
    else:
        pass

    print('O modulo de redes levou: {} para mapear a rede e coletar informações de portas para cada IP'.format(datetime.now() - timeStart))

def retorna_info_hosts():
    # exec_info_redes()
    if len(enderecos_ativos) == 0:
        return False
    else:
        return enderecos_ativos

exec_info_redes_async = sync_to_async(exec_info_redes, thread_sensitive=False)
