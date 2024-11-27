#Vicente Yahir Lopez Vazquez - 240010


numeros = []

for i in range(5):
    numero = float(input(f"ingrese un número: "))
    numeros.append(numero)

numsinv = numeros[::-1]

print("\nlos números ingresados fueron:", numeros)
print("los números en orden inverso son:", numsinv)
