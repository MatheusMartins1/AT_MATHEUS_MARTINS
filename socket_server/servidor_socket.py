import socket
import pickle
from gerenciador_pc.CONSTANTES import HOST, PORTA
from pc import PC
from processos import retorna_processos
from arquivos import retorna_arquivos
from rede import *


async def exec_server():
    # Cria o socket
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((HOST, PORTA))
    socket_servidor.listen()

    while True:
        try:

            print("Servidor de nome", HOST, "esperando conexão na porta", PORTA)

            resposta = False
            (socket_cliente, addr) = socket_servidor.accept()
            print("\nConectado a:", socket_cliente, str(addr))

            msg = socket_cliente.recv(1024)
            msg = msg.decode('utf-8')

            # Gera a lista de resposta
            print("obj:", msg)
            if msg == "pc":
                resposta = PC()
            elif msg == "processos":
                resposta = retorna_processos()
            elif msg == "rede":
                resposta = retorna_info_hosts()
            elif "arquivos" in msg:
                caminho = msg.split(";")[1]
                print(f"\nCaminho:{caminho}")
                resposta = retorna_arquivos(caminho)

            if resposta:
                # Prepara a lista para o envio
                bytes_resp = pickle.dumps(resposta)

                # Envia os dados
                socket_cliente.send(bytes_resp)
                print("enviado")

            while msg == "fim":
                # socket_cliente.send(resp.encode('utf-8'))
                socket_cliente.close()

        except Exception as e:
            print(e)

loop = asyncio.get_event_loop()

loop.create_task(retorna_interfaces_redes_async())
loop.create_task(exec_info_redes_async())
loop.run_until_complete(exec_server())

loop.close()
