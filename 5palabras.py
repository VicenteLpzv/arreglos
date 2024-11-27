#Vicente Yahir Lopez Vazquez - 240010
#ordenar alfabeticamente las palabras

palabras = []
for i in range(1,6):
    palabra = (input("Ingresa una palabra: "))
    
    palabras.append(palabra)
    
    
palabras.sort()
print("Palabras ordenadas alfabéticamente:", palabras)