import socket
serverIP = "127.0.0.10"
serverPort = 10000
maxBytes = 4096
sock = 
socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
sock.bind((serverIP, 
serverPort))
sock.listen()