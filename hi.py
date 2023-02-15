import socket

server = socket.socket()
host = '127.0.0.1' #L'IP du Serveur
port = 1234
server.connect((host,port))

msg =server.recv(1024)
print(msg.decode('UTF-8'))

server.send('Client Online ...'.encode('UTF-8'))
input()
