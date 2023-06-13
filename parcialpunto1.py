def obtener_palabras_repetidas(vector):
    palabras_repetidas = {}

    if len(vector) == 0:
        return palabras_repetidas

    palabra_actual = vector[0]
    resto_vector = vector[1:]

    if palabra_actual in resto_vector:
        if palabra_actual not in palabras_repetidas:
            palabras_repetidas[palabra_actual] = resto_vector.count(palabra_actual) + 1

    palabras_repetidas.update(obtener_palabras_repetidas(resto_vector))

    return palabras_repetidas


vector_palabras = ["eso", "tilin", "eso", "tilin", "eso", "papu", "tilin"]
palabras_repetidas = obtener_palabras_repetidas(vector_palabras)
print("Palabras repetidas:")
for palabra, cantidad in palabras_repetidas.items():
    print(palabra, "- Repeticiones:", cantidad)
