import psutil
import time
from funcoes import formata_tamanho

def retorna_processos():
    processos = {}

    processos_ativos = psutil.pids()
    nome_processos = []
    for proc in processos_ativos:
        try:
            processo = psutil.Process(proc)
            nome_processo = processo.name()

            if nome_processo not in nome_processos:
                processos[proc] = {}
                processos[proc]["pid"] = processo.pid
                processos[proc]["nome"] = nome_processo
                processos[proc]["status"] = processo.status()
                processos[proc]["dt_inicio"] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(processo.create_time())) if getattr(processo,"started",'') == "" else ""
                processos[proc]["tempo_exec"] = time.strftime("%H:%M:%S", time.localtime(time.time() - processo.create_time()))
                processos[proc]["tempo_user"] = time.strftime("%H:%M:%S", time.localtime(time.time() - processo.cpu_times().user))
                processos[proc]["tempo_system"] = time.strftime("%H:%M:%S", time.localtime(time.time() - processo.cpu_times().system))
                processos[proc]["memoria"] = processo.memory_info()[1]
                processos[proc]["memoria_uso"] = processo.memory_percent()
                processos[proc]["threads"] = processo.num_threads()

                nome_processos.append(nome_processo)
            else:
                processos[proc]["memoria"] += processo.memory_info()[1]
                processos[proc]["memoria_uso"] += processo.memory_percent()
                processos[proc]["threads"] += processo.num_threads()

        except Exception:
            pass

    processos = [i[1] for i in sorted(processos.items(), key=lambda x: x[1]['memoria'], reverse=True)] #ordenando por memoria

    processos_retorno = {}
    for p in processos:
        index = processos.index(p)
        if index < 30: #Mantendo somente os 30 primeiros
            processos_retorno[index] = p
            processos_retorno[index]["memoria"] = formata_tamanho(p["memoria"])
            processos_retorno[index]["memoria_uso"] = round(p["memoria_uso"],2)

    return processos_retorno