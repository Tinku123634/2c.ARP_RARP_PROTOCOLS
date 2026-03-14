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