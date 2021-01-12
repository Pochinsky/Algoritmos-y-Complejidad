from math import inf
import sys

"""
Function:    get_array.
Parameters:  string filename: nombre del archivo a leer.
Return:      list array: lista con los elementos del arreglo.
Description: obtiene el arreglo desde el
             archivo entregado.
"""
def get_array(filename):
    arch = open(filename, "r")
    for line in arch:
        line = line.strip()
        if len(line) == 1:
            n = int(line)
        else:
            arr = line.split(" ")
            array = list()
            for number in arr:
                array.append(int(number))
    return array                
"""
Function:       maximum.
Parameters:     list array: arreglo de enteros positivos.
Return:         int big: mayor numero del arreglo.
Description:    obtiene el mayor numero del arreglo.
execution time: Theta(n)
"""
def maximum(array):
    big = -1
    for number in array:
        if number > big:
            big = number
    return big

"""
Function:       minimum.
Parameters:     list array: arreglo de enteros positivos.
Return:         int small: menor numero del arreglo.
Description:    obtiene el menor numero del arreglo.
execution time: Theta(n)
"""
def minimum(array):
    small = inf
    for number in array:
        if number < small:
            small = number
    return small            

def get_subarray(array, start, end):
    subarray = list()
    while start <= end:
        subarray.append(array[start])
        start += 1
    return subarray        

def sum_of_imbalance(array, start, end):
    if start == end:
        return 0
    else:
        medium  =  (start + end) // 2
        total   =  sum_of_imbalance(array, start, medium)
        total   += sum_of_imbalance(array, medium+1, end)
        aux     =  get_subarray(array, start, end)
        total   += maximum(aux) - minimum(aux)
        aux     =  get_subarray(array, medium, end)
        total   += maximum(aux) - minimum(aux)
        return total

def main():
    A = get_array(sys.argv[1])
    print(sum_of_imbalance(A, 0, len(A)-1))

if __name__=="__main__":
    if len(sys.argv) >= 2:
        main()
    else:
        print("=== ERROR ===")
        print("Argumentos de programa insuficientes.")
        print("Programa finalizado.")

