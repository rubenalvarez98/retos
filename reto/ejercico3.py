def cambio_minimo(coins):
    # Ordena el array de monedas en orden ascendente
    coins.sort()

    # Inicializa el monto mínimo de cambio que queremos formar
    cambio_min = 1

    # Recorre cada moneda en el array ordenado
    for moneda in coins:
        # Si la moneda es menor o igual al monto mínimo actual que queremos formar
        if moneda <= cambio_min:
            # Aumenta el monto mínimo que podemos formar agregando el valor de la moneda
            cambio_min += moneda
        else:
            # Si la moneda es mayor que el monto mínimo actual que queremos formar,
            # no podemos formar el monto actual con las monedas disponibles.
            # Entonces, terminamos el bucle.
            break

    # Devuelve el monto mínimo que no se puede formar con las monedas disponibles
    return cambio_min

# Ejemplos de uso del algoritmo

monedas1 = [5, 7, 1, 1, 2, 3, 22]
# Llama a la función con el primer conjunto de monedas
resultado1 = cambio_minimo(monedas1)
print(f"El cambio mínimo es: {resultado1}")  # Esperado: 20

monedas2 = [1, 1, 1, 1, 1]
# Llama a la función con el segundo conjunto de monedas
resultado2 = cambio_minimo(monedas2)
print(f"El cambio mínimo es: {resultado2}")  # Esperado: 6

monedas3 = [1, 5, 1, 1, 1, 10, 15, 20, 100]
# Llama a la función con el tercer conjunto de monedas
resultado3 = cambio_minimo(monedas3)
print(f"El cambio mínimo es: {resultado3}")  # Esperado: 55
