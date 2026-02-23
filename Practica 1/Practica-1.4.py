import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #más info abajo del todo
server.bind((HOST, PORT))
server.listen(1)  #solo puede haber un cliente en cola mientras otro hace accept - recv - send -close

print(f"Servidor en http://{HOST}:{PORT}")

try:
    while True:
        client, addr = server.accept()    #objeto socket (es el canal, nos permite hacer recv y send), y tupla (ip, puerto)
        request = client.recv(4096).decode(errors="ignore")

        #extrae URL
        primera_linea = request.split("\r\n")[0]
        #request.split("\r\n") → devuelve lista de strings (cada línea de la petición). coge el primero y devuelve un string.
        partes = primera_linea.split()  #separa por espacio en blanco si no se pone argumento.  Partes es una list
        url = partes[1] if len(partes) > 1 else "/"

        #extrae User-Agent
        user_agent = "desconocido"
        for linea in request.split("\r\n"):        #recorre cada linea del request
            if linea.lower().startswith("user-agent:"):
                user_agent = linea.split(":", 1)[1].strip()   #divide la línea en dos partes por el primer :. strip - quita espacios al inicio y final
                break

        #cuerpo de respuesta
        cuerpo = f"""
        Hola!
        URL pedida: {url}
        Browser: {user_agent}
        """
        cuerpo = cuerpo.rstrip()

        respuesta = (
	    "HTTP/1.1 200 OK\r\n"
	    "Content-Type: text/plain\r\n"
	    f"Content-Length: {len(cuerpo)}\r\n"
	    "\r\n"
	    + cuerpo
        )

        client.sendall(respuesta.encode())
        client.close()    #cierra la conexion solo con el cliente
	
except KeyboardInterrupt:
	    print("\nServidor detenido por el usuario.")
	    server.close()  #aqui cierra el socket del servidor que estaba escuchando, ya no acepta nuevas conexiones en el 8080


#para probar:
#Primero ejecutamos el script
#Luego ponemos esto en el navegador o terminal: curl http://127.0.0.1:8080/hola





#antes del bind -- server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#El puerto puede seguir “ocupado” aunque cerremos el servidor o Ctrl+C, porque TCP deja la dirección en TIME_WAIT. Usar SO_REUSEADDR permite reiniciar inmediatamente.
