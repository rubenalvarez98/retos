def reorganizar_y_filtrar(numeros, S):
    # Crear una lista vacía para almacenar los números después de filtrar los dígitos >= S
    numeros_filtrados = []

    # Iterar sobre cada número en la lista original
    for numero in numeros:
        # Convertir el número en una cadena de caracteres para poder trabajar con cada dígito
        numero_str = str(numero)
        numero_filtrado_str = ""

        # Iterar sobre cada carácter (dígito) en la representación de cadena del número
        for caracter_digito in numero_str:
            # Convertir el carácter a un dígito (entero)
            digito = int(caracter_digito)

            # Si el dígito es menor que S, lo añadimos a la nueva cadena filtrada
            if digito < S:
                numero_filtrado_str += caracter_digito

        # Si después del filtrado la cadena no está vacía, convertirla en número y añadirla a la lista filtrada
        if numero_filtrado_str:
            numeros_filtrados.append(int(numero_filtrado_str))

    # Implementación manual de la ordenación en orden descendente (Bubble Sort)
    n = len(numeros_filtrados)
    for i in range(n):
        for j in range(0, n-i-1):
            # Comparar elementos consecutivos y cambiarlos si están en el orden incorrecto
            if numeros_filtrados[j] < numeros_filtrados[j+1]:
                numeros_filtrados[j], numeros_filtrados[j+1] = numeros_filtrados[j+1], numeros_filtrados[j]

    # Devolver la lista filtrada y ordenada
    return numeros_filtrados

# Ejemplos de prueba
print(reorganizar_y_filtrar([1, 2, 3, 4, 5, 6,7], 7))
print(reorganizar_y_filtrar([10, 20, 30, 40], 7))
print(reorganizar_y_filtrar([6], 7))
print(reorganizar_y_filtrar([77], 7))
print(reorganizar_y_filtrar([65], 7))
print(reorganizar_y_filtrar([6, 2, 1], 7))
print(reorganizar_y_filtrar([60, 6, 5, 4, 3, 2, 7, 7, 29, 1], 7))

