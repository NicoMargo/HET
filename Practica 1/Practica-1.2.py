import sys

#python Practica-1.2.py /etc/passwd

if len(sys.argv) != 2:
    print("Uso: python Practica-1.2.py <ruta_del_fichero>")
    sys.exit(1)

ruta = sys.argv[1]

try:
    with open(ruta, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")
except PermissionError:
    print("Permiso denegado. Ejecuta la terminal como administrador.")
