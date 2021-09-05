import socket
import pickle
import sys
from gerenciador_pc.CONSTANTES import HOST,PORTA
from socket_server import pc
sys.modules['pc'] = pc


def requisita_servidor_socket(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resposta = ""
    try:
        print(f"\nSocket conectando ao servidor em {HOST}:{PORTA} requisitando {msg}")
        s.connect((HOST, PORTA))

        s.send(msg.encode('utf-8'))

        bytes = s.recv(4096)

        resposta = pickle.loads(bytes, fix_imports=True, encoding="utf-8")

    except Exception as erro:
        print("erro:",str(erro))

    print("fim conexão socket\n")
    s.close()
    
    return resposta


# CD "D:\Users\Matheus\Documents\workspacePython\AT_MATHEUS_MARTINS\gerenciador_pc\socket"
# python cliente_socket.py