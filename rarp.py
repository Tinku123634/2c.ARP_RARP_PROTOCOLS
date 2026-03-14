import socket

s = socket.socket()
s.connect(("localhost", 9000))

while True:
    ip = input("Enter IP address to get MAC (or 'exit'): ")

    if ip == "exit":
        break

    s.send(ip.encode())
    mac = s.recv(1024).decode()

    print("MAC Address:", mac)

s.close()