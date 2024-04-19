import socket

def send_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))
    while True:
        message = input("Enter message: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print("Server response:", data.decode())

if __name__ == "__main__":
    send_message()
