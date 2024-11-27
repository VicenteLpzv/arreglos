#Vicente Yahir Lopez Vazquez - 240010

numeros = []

for i in range(1,6):
    numero = float(input("ingresa algun numero aleatorio: "))
    numeros.append((numero))
    
min(numeros)
max(numeros)

print (numeros)
print (f"el numero minimo es: {min(numeros)}")

print (f"el numero maximo es: {max(numeros)}")
