import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor en http://{HOST}:{PORT}")

while True:
    client, addr = server.accept()

    request = client.recv(4096).decode(errors="ignore")

    # ---- extraer URL ----
    primera_linea = request.split("\r\n")[0]
    partes = primera_linea.split()
    url = partes[1] if len(partes) > 1 else "/"

    # ---- extraer User-Agent ----
    user_agent = "desconocido"
    for linea in request.split("\r\n"):
        if linea.startswith("User-Agent:"):
            user_agent = linea.split(":", 1)[1].strip()
            break

    # ---- cuerpo de respuesta ----
    cuerpo = f"""Hola!
URL pedida: {url}
Browser: {user_agent}
"""

    respuesta = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(cuerpo)}\r\n"
        "\r\n"
        + cuerpo
    )

    client.sendall(respuesta.encode())
    client.close()



#para probar:
#Primero ejecutamos el script
#Luego ponemos esto en el navegador o terminal: curl http://127.0.0.1:8080/hola
