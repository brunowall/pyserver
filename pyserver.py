import socket;
import threading


def listen(port): 
	socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria socket tcp
	socketserver.bind(("",port)); # escuta em todas as interfaces
	socketserver.listen(5);
	while True: # escuta em loop infinito 
		connect, client = socketserver.accept();
		threading.Thread(name='threadcliente', target=handle(connect,client))
	

def handle(connect,client):
	arquivo = open('index.html', 'r+') # abre o arquivo para somente leitura
	content = arquivo.read();
	while True:
		msg = connect.recv(4*1024) #recebe 4KB de uma vez		
		buffer = ("HTTP/1.1 200 OK \r\n" + "Content-Type: text/html \r\n\r\n" + content);
		connect.send(buffer)

	arquivo.close();
	connect.close();
				
listen(8000)