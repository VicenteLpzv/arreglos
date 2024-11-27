#Vicente Yahir Lopez Vazquez - 240010

letras = []

for i in range(5):
    letra = input(f"ingrese la letra {i + 1}: ")
    # Asegurarse de que el usuario ingrese solo una letra
    while len(letra) != 1 or not letra.isalpha():
        letra = input("ingrese solo una letra: ")
    letras.append(letra.lower())  

letrabuscar = input("\ningrese una letra para buscarla: ")

conteo = letras.count(letrabuscar)

print("\nlas letras ingresadas fueron:", letras)
print(f"la letra '{letrabuscar}' aparece {conteo} veces en el arreglo.")
