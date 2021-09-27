from socket import *

SERVER_IP = "localhost"
SERVER_PORT = 1111

s = socket(AF_INET, SOCK_STREAM)
s.bind((SERVER_IP, SERVER_PORT))
s.listen(1)
print(f"Server now running on {SERVER_IP}:{SERVER_PORT}")

client, addr = s.accept()
print(f"Connected to {addr}")

while True:
    request = input("Request > ").encode()
    option = input("Have a answer from client ? ")
    if request:
        client.send(request)
        if not option == "":
            data = client.recv(123456789).decode()
            print(data)

client.close()