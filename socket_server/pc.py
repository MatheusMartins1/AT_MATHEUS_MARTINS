import psutil
import cpuinfo
from socket_server.funcoes import formata_tamanho

class PC:
    def __init__(self):
        self.IP = psutil.net_if_addrs()['Ethernet'][1][1]
        self.memoria = self.retorna_memoria()
        self.disco = self.retorna_disco()
        self.CPU = self.retorna_CPU()

    def retorna_disco(self):
        disco = psutil.disk_usage('../gerenciador_pc/cliente_socket')
        percent_uso = round(((disco.used/disco.total)*100), 2)
        disco = {
            "Total" : formata_tamanho(disco.total)
            ,"Em uso" : formata_tamanho(disco.used)
            ,"percent_uso" : percent_uso
            ,"Livre" :formata_tamanho(disco.free)
            ,"percent_livre" : round(100-percent_uso, 2)
        }
        return disco

    def retorna_memoria(self):
        memoria = psutil.virtual_memory()
        total = formata_tamanho(memoria.total)
        return memoria.percent,total

    def retorna_CPU(self):
        info_cpu = cpuinfo.get_cpu_info()
        capacidade = psutil.cpu_percent(interval=0)
        frequencia = str(round(psutil.cpu_freq().current, 2))
        cpu = {
        "Processador": f"{info_cpu['brand_raw']} {info_cpu['bits']} bits"
        ,"Utilização": f"{capacidade} %"
        ,"Arquitetura": info_cpu['arch']
        ,"Frequência" : f"{frequencia} (MHz)"
        ,"Núcleos": f"{psutil.cpu_count()} ({str(psutil.cpu_count(logical=False))})"
        }
        return cpu
