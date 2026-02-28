#!/usr/bin/env python3

# Importa el módulo base64, que nos da las herramientas para decodificar (y codificar) texto o archivos.
import base64

# Esto hace que trabajar con rutas de archivos y leerlos sea mucho más fácil y moderno.
from pathlib import Path

# 1. Path("passwd64") apunta al archivo llamado "passwd64" en la misma carpeta.
# 2. .read_bytes() abre ese archivo, lee todo su contenido en formato binario (bytes) 
#    y lo guarda en la variable 'b64_data'.
b64_data = Path("passwd64").read_bytes()

# Toma esos bytes que están codificados en base64 y los decodifica a su forma original.
# El resultado son los datos crudos (raw bytes) y se guardan en la variable 'raw'.
raw = base64.b64decode(b64_data)

# 1. raw.decode("utf-8") convierte los bytes crudos a texto normal, usando el formato UTF-8.
# 3. end="" hace que la función print() no añada un salto de línea extra al final de lo que imprime.
print(raw.decode("utf-8", errors="replace"), end="")
