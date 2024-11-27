#Vicente Yahir Lopez Vazquez - 240010
#Decir si el arreglo está ordenado de mayor o menor o decir si no lo está

numeros = []

for i in range(6):
    numero = float(input(f"ingrese el número {i + 1}: "))
    numeros.append(numero)

# Verificar si el arreglo está ordenado de menor a mayor
ordenado = numeros == sorted(numeros)

print("\nLos números ingresados son:", numeros)
if ordenado:
    print("El arreglo está ordenado de menor a mayor.")
else:
    print("El arreglo NO está ordenado de menor a mayor.")
