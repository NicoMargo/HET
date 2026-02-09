import sys

#python W:\HET\imprimir_archivo.py C:\Windows\System32\drivers\etc\hosts   comentario

if len(sys.argv) != 2:
    print("Uso: python imprimir_archivo.py <ruta_del_fichero>")
    sys.exit(1)

ruta = sys.argv[1]

try:
    with open(ruta, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")
except PermissionError:
    print("Permiso denegado. Ejecuta la terminal como administrador.")
