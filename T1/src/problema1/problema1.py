import sys
from function import *

def main():
    resultado   = []
    archivo     = open(sys.argv[1],'r')
    for line in archivo:
        resultado   = []
        datos       = line.strip('\n').split(' ')
        if datos[0] == '0':
            exit()
        objetivo = int(datos[0])
        print(f'Suma de {objetivo}: ')
        datos.pop(0)
        datos.pop(0)
        lista = []
        for dato in datos:
            lista.append(int(dato))
        posibles = sub_listas(lista)
        for posible in posibles:
            if suma_lista(posible) == objetivo:
                if posible not in resultado:
                    resultado.append(posible)
        if resultado == []:
            print('NADA')
        for suma in resultado:
            if len(suma) == 1:
                print(suma[0])
            else:
                flag    = True
                salida  = ''
                for num in suma:
                    if flag:
                        salida += str(num)
                        flag    = False
                    else:
                        salida += '+'+str(num)
                print(salida)

if __name__=="__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("=== ERROR ===")
        print("ingrese:")
        print("python problema1.py input.dat")
