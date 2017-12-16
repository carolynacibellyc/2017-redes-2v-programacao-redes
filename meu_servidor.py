import socket
ip = 'localhost'
porta = 2001

x = b"Israel #1 Carol #2"
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind ((ip,porta))
servidor.listen(5)
nome,endereço = servidor.accept()

while True:
	dados = nome.recv(1024)
	msg_decode = dados.decode("ASCII")
	if msg_decode == 'candidatos?':
		nome.send(x)

