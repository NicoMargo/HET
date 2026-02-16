import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)  #solo puede haber un cliente en cola mientras otro hace accept - recv - send -close

print(f"Servidor en http://{HOST}:{PORT}")

while True:
    client, addr = server.accept()     #objeto socket (es el canal, nos permite hacer recv y send), y tupla (ip, puerto) (nos dice quien es)

    request = client.recv(4096).decode(errors="ignore")

    #extrae URL
    primera_linea = request.split("\r\n")[0]
    #request.split("\r\n") → devuelve lista de strings (cada línea de la petición). coge el primero y devuelve un string.
    partes = primera_linea.split()  #separa por espacio en blanco si no se pone argumento.  Partes e suna list
    url = partes[1] if len(partes) > 1 else "/"

    #extrae User-Agent
    user_agent = "desconocido"
    for linea in request.split("\r\n"):        #recorre cada linea del request
        if linea.startswith("User-Agent:"):
            user_agent = linea.split(":", 1)[1].strip()   #divide la línea en dos partes por el primer :. strip - quita espacios al inicio y final
            break

    #cuerpo de respuesta
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
