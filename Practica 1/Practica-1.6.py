import sys
import struct

if len(sys.argv) != 2:
    print("Uso: python script.py numero")
    sys.exit(1)

n = int(sys.argv[1])

b1 = struct.pack("B", n & 0xff)        # 1 byte
b2 = struct.pack("<H", n & 0xffff)     # 2 bytes
b4 = struct.pack("<I", n & 0xffffffff) # 4 bytes

# escribir bytes crudos a stdout
sys.stdout.buffer.write(b1 + b2 + b4)




#B → entero sin signo de 1 byte
#H → entero de 2 bytes
#I → entero de 4 bytes
#< → little-endian (orden de bytes típico en x86)
#& 0xff etc evita errores si el número es muy grande.

#para probar: python script.py 300 | hd
