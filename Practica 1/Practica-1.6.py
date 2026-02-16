import sys
import struct

if len(sys.argv) != 2:
    print("Pon: python script.py numero")
    sys.exit(1)

n = int(sys.argv[1])

b1 = struct.pack("B", n & 0xff)        # 1 byte, mira solo el ultimo byte de n
b2 = struct.pack("<H", n & 0xffff)     # 2 bytes, los dos ultimos bytes
b4 = struct.pack("<I", n & 0xffffffff) # 4 bytes 

# escribir bytes crudos a stdout
sys.stdout.buffer.write(b1 + b2 + b4)




#B → entero sin signo de 1 byte
#H → entero de 2 bytes
#I → entero de 4 bytes     ejemplo:0x0000012C

#< → little-endian (primero el byte más bajo)  ---------- si es 0x012C entonces --- Primer byte = 0x2C, segundo = 0x01

#& 0xff etc evita errores si el número es muy grande.

#hd

#para probar: python script.py 300 | hd
