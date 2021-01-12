import sys
from graph import *
from function import *

"""
Function    : main
Description : controla la ejecución principal
              del programa
"""
def main():
    lands          = list()
    auxLands       = list()
    points         = list()
    auxPoints      = list()
    lista_tupeable = list()

    # extract number of cases
    arch = open(sys.argv[1], "r")
    n = int(arch.readline().strip())
    arch.readline()

    # extract all cases
    while n > 0:
        line = arch.readline().strip()
        if line == "":
            n -= 1
            lands.append(auxLands)
            points.append(auxPoints)
            auxLands  = list()
            auxPoints = list()
        elif line[0] not in '123456789':
            auxLands.append(list(line))
        else:
            lista_tupeable.append(int(line[0]))
            lista_tupeable.append(int(line[2]))
            auxPoints.append(tuple(lista_tupeable))
            lista_tupeable = list()
    arch.close()

    # all cases
    for land in lands:
        # one case
        N = len(land)    # number of rows
        M = len(land[0]) # number of columns

        G = Graph(N,M)
        G.fillGraph(N,M,land)
        for point in points[lands.index(land)]:
            print(getArea(G,point))
        print("")

if __name__=="__main__":
    if len(sys.argv)==2:
        main()
    else:
        print("=== ERROR ===")
        print("Ingrese:")
        print("python problema2.py input.txt")
