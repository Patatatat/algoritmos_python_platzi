import random

def ordenamiento_por_insercion(lista):
    indice = len(lista)
    count = 0

    for indice in range(1, len(lista)):
        count += 1
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    
    print(f'Se realizaron {count} movimientos!' )
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista?'))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
  
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)