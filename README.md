# 2c.SIMULATING ARP /RARP PROTOCOLS
## AIM
To write a python program for simulating ARP protocols using TCP.
## ALGORITHM:

1.Create an ARP table in the server with IP and MAC address mappings.

2.Establish a TCP socket connection between the client and server.

3.The client sends an IP address request to the server.

4.The server searches the ARP table and sends the corresponding MAC address to the client.

5.The client displays the MAC address and the connection is closed after completion.

## Client:
1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
## Server:
1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.
P
## PROGRAM - ARP
~~~
import socket

arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03"
}

s = socket.socket()
s.bind(("localhost", 9000))
s.listen(1)

print("ARP Server waiting for connection...")

conn, addr = s.accept()
print("Connected to", addr)

while True:
    ip = conn.recv(1024).decode()
    if not ip:
        break

    print("ARP Request for IP:", ip)

    mac = arp_table.get(ip, "IP not found in ARP table")
    conn.send(mac.encode())

conn.close()
s.close()
~~~



## OUPUT - ARP
![alt text](<Screenshot 2026-03-14 090426.png>)

## PROGRAM - RARP
~~~
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
~~~
## OUPUT -RARP
![alt text](<Screenshot 2026-03-14 090441-1.png>)
## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully 
executed.
