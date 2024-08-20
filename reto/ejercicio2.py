def cuadrados_ordenados(array, S):
    cuadrados_validos = []  # Lista vacía para almacenar los cuadrados válidos dentro del rango

    for numero in array:  # Itera sobre cada número en el arreglo original
        cuadrado = numero * numero  # Calcula el cuadrado del número
        if 0 <= cuadrado <= S**2:  # Verifica si el cuadrado está dentro del rango [0, S^2]
            cuadrados_validos.append(cuadrado)  # Agrega el cuadrado a la lista de válidos

    # Función interna para ordenar la lista usando el algoritmo de ordenamiento por burbuja
    def bubble_sort(lst):
        n = len(lst)  # Obtiene el tamaño de la lista
        # Recorre toda la lista
        for i in range(n):
            # Recorre la lista hasta el penúltimo elemento no ordenado
            for j in range(0, n-i-1):
                # Compara el elemento actual con el siguiente
                if lst[j] > lst[j+1]:
                    # Si el elemento actual es mayor que el siguiente, intercámbialos
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        # Devuelve la lista ordenada
        return lst

    return bubble_sort(cuadrados_validos)  # Ordena la lista de cuadrados válidos y la devuelve

# Pruebas
entrada_1 = [1, 2, 3, 5, 6, 8, 9]
resultado_1 = cuadrados_ordenados(entrada_1, 7)
print(resultado_1)  # Output esperado: [1, 4, 9, 25, 36]

entrada_2 = [-2, -1]
resultado_2 = cuadrados_ordenados(entrada_2, 7)
print(resultado_2)  # Output esperado: [1, 4]

entrada_3 = [-6, -5, 0, 5, 6]
resultado_3 = cuadrados_ordenados(entrada_3, 7)
print(resultado_3)  # Output esperado: [0, 25, 25, 36, 36]

entrada_4 = [-10, 10]
resultado_4 = cuadrados_ordenados(entrada_4, 7)
print(resultado_4)  # Output esperado: []



