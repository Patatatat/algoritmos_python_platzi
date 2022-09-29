# import random

# def busqueda_binaria(lista, comienzo, final, objetivo):
#    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
#    if comienzo > final:
#        return False
#   medio = (comienzo + final) // 2
#
#   if lista[medio] == objetivo:
#       return True
#    elif lista[medio] < objetivo:
#        return busqueda_binaria(lista, medio + 1, final, objetivo)
#    else:
#        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
#
# if __name__ == '__main__':
#    tamano_de_la_lista = int(input('De que tamano sera la lista?'))
#    objetivo = int(input('Que numero quieres encontrar? '))
#
#    lista = sorted([random.randint(0, 100) for i in range(tamano_de_la_lista)])
#
#    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
#    print(lista)
#    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => 1