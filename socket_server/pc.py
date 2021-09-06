import psutil
import cpuinfo
try:
    from funcoes import formata_tamanho
except:
    from socket_server.funcoes import formata_tamanho

class PC:
    def __init__(self):
        self.IP = psutil.net_if_addrs()['Ethernet'][1][1]
        self.memoria = self.retorna_memoria()
        self.disco = self.retorna_disco()
        self.CPU = self.retorna_CPU()
        self.processador = self.retorna_CPU_node()

    def retorna_disco(self):
        disco = psutil.disk_usage('.')
        percent_uso = round(((disco.used/disco.total)*100), 2)
        disco = {
            "Total" : formata_tamanho(disco.total)
            ,"uso" : formata_tamanho(disco.used)
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
        utilizacao = psutil.cpu_percent(interval=0)
        uso = info_cpu['hz_advertised'][0] - (float(f"0.{str(utilizacao).replace('.','')}") * info_cpu['hz_advertised'][0])
        uso = str(str(uso)[:1] + ',' + str(uso)[2:])[:4]
        cpu = {
        "Processador": f"{info_cpu['brand_raw']} {info_cpu['bits']} bits"
        ,"Utilização": f"{round(utilizacao,1)}% ({uso}GHz) | Total: {info_cpu['hz_advertised_friendly'][:3]}GHz"
        ,"Arquitetura": info_cpu['arch']
        ,"Frequência" : f"{str(round(psutil.cpu_freq().current, 2))} (MHz)"
        ,"Núcleos": f"Lógicos: {psutil.cpu_count()} | Físicos: {str(psutil.cpu_count(logical=False))}"
        }
        return cpu
    
    def retorna_CPU_node(self):
        uso_cpu = {}
        nodes = psutil.cpu_percent(interval=0,percpu=True)

        for n in range(0,psutil.cpu_count()):
            node = n+1
            uso_cpu[node] = nodes[n]

        return uso_cpu
