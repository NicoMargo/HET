x = 5
y = 4.5

palabra = "hola\n"

texto = """esto 
es una frase 
con salto integrado\n"""

lista_mutable = [1,2,3,4]
lista_mutable[1] = 20

lista_inmutable = (10,20,30,40)

diccionario = {
    "ciudad": "Valencia"
}

#para acceder a uno es diccionario["ciudad"]


conjunto = {1,2,3,3,3,3}


print(x)
print(y)
print(palabra)
print(texto)
print(lista_mutable)
print(lista_inmutable)
print(diccionario)
print(conjunto)

#
print("\nRecorriendo lista_mutable:")

for num in lista_mutable:
    print("Valor actual:", num)

    if num % 2 == 0:
        print("es par")
    else:
        print("es impar")



#diccionario
print("\nDiccionario:")
for clave, valor in diccionario.items():
    print("Clave:", clave, "Valor:", valor)



#rango
print("\nBucle con rango:")  
for i in range(x):            #Es lo mismo que range(0,x)
    print("i =", i)


#print(conjunto)

