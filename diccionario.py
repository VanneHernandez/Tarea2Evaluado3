#Diccionario con algunas palabras y sus definiciones
diccionario = {
    "python": "Un lenguaje de programación de alto nivel.",
    "variable": "Un espacio en memoria donde se almacena un valor.",
    "función": "Un bloque de código que realiza una tarea específica.",
    "bucles": "Estructuras de control que repiten un bloque de código.",
    "list": "Una estructura de datos que almacena una secuencia de elementos."
}

# Función para buscar una palabra en el diccionario
def buscar_palabra(palabra):
    if palabra in diccionario:
        return diccionario[palabra]
    else:
        return "La palabra no está en el diccionario."

# Menú de opciones
def menu():
    print("Bienvenido al diccionario interactivo.")
    while True:
        palabra = input("Ingresa una palabra para buscar su significado (o 'salir' para terminar): ").lower()
        if palabra == 'salir':
            print("¡Hasta luego!")
            break
        significado = buscar_palabra(palabra)
        print(f"Definición de '{palabra}': {significado}")

# Ejecutar el menú
menu()
