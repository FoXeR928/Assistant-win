import socket

def socket_init():
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.0', 59000))

    message = input(" -> ")

    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    client_socket.close()