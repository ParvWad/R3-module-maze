import socket


TCP_IP = '192.168.2.78'
TCP_PORT = 80
BUFFER_SIZE = 1024  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE).decode()
    if not data: break
    print ("received data:", data)
conn.close()
