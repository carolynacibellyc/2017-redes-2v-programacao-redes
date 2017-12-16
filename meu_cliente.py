import socket
ip = "127.0.0.1"
porta = 2001
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
msg="candidatos?"
cliente.connect((ip,porta))
codificada = msg.encode("utf-8")
cliente.send(codificada)
dados = cliente.recv(1024)
dados = dados.decode ("ascii")
print(dados)
