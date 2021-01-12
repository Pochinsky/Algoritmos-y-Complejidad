"""
Function    : suma_lista
Parameters  : list lista
Description : suma todos los elementos de una lista
Return      : suma total
"""    
def suma_lista(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma

"""
Function    : sub_listas
Parameters  : list lista
Description : genera todas las sublistas posibles
              con backtracking
Return      : lista de todas las sublistas
"""
def sub_listas(lista):
    resultado = []
    backtracking(resultado, [], lista, 0)
    return resultado

"""
Function    : backtracking
Parameters  : int resultado, list aux, list lista, int inicio
Description : procedimiento de backtracking
Return      : no retorna
"""
def backtracking(resultado, aux, lista, inicio):
    resultado.append(aux[:])
    for i in range(inicio, len(lista)):
        aux.append(lista[i])
        backtracking(resultado, aux, lista, i + 1)
        aux.pop()

