import socket

host = "www.upv.es"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #ipv4 y tcp -----------#inetv6 y dgram para udp

s.settimeout(5)  #5 segundos

s.connect((host, port))

peticion = "GET / HTTP/1.1\r\nHost: www.upv.es\r\n\r\n"
s.send(peticion.encode())  #por defecto es encode("UTF-8")


response = b""  # inicializar bytes
try:
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
except socket.timeout:
    print("Timeout al recibir la respuestaaaa")

print(response.decode(errors="ignore"))

s.close()
