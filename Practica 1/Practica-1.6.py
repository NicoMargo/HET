import sys
import struct

# sys.argv guarda los argumentos de la línea de comandos. 
if len(sys.argv) != 2:
    print("Uso correcto: python script.py <numero>")
    sys.exit(1)

# Convertimos el argumento (que entra como texto) a un número entero.
n = int(sys.argv[1])

# -- UN BYTE --
# "B" significa entero sin signo de 1 byte (unsigned char en C).
# 'n & 0xff' (máscara AND a nivel de bits) fuerza a que solo miremos los últimos 8 bits.
# Si metes un número mayor a 255 (ej. 300), esto evita que la función lance un error,
# simplemente truncará el número y se quedará con la parte que cabe en 1 byte.
b1 = struct.pack("B", n & 0xff)        

# -- DOS BYTES --
# "<H" significa entero sin signo de 2 bytes (unsigned short).
# El símbolo "<" indica "Little-Endian" (el byte menos significativo se guarda primero).
# 'n & 0xffff' limita el valor a 16 bits.
b2 = struct.pack("<H", n & 0xffff)     

# -- CUATRO BYTES --
# "<I" significa entero sin signo de 4 bytes (unsigned int).
# También en Little-Endian.
# 'n & 0xffffffff' limita el valor a 32 bits.
b4 = struct.pack("<I", n & 0xffffffff) 

# sys.stdout.buffer.write() nos permite volcar los datos binarios crudos (raw) directamente.
# Aquí concatenamos (sumamos) los bytes de 1, 2 y 4 tamaños y los enviamos.
sys.stdout.buffer.write(b1 + b2 + b4)
