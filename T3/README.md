## Algoritmos y Complejidad

# Tarea3

### El mínimo esfuerzo necesario para ordenar un arreglo

Sea un arreglo `A` de `n` enteros, con `1<=n<=1000000`.

Se quiere ordenar `A` utilizando el mínimo número de pasos posibles.

- Un paso consiste en cambiar una entrada en la posición `A[i]`, con `i=0,...,n-1` a otra posición `A[j]`, con `j=0,...,n-1` y `i!=j`.

**Objetivo**

Crear un algoritmo de programación dinámica que cuente la cantidad mínima de pasos para ordenar `A`.

**Entrada**

Archivo

- Cada línea contiene `n+1` números enteros separados por espacio de forma tal que el primer número es `n` e indica la cantidad de elementos del arreglo y seguido de a el, le continuan los `n` números enteros del arreglo.

**Salida**

Consola

- Cada línea muestra un único entero correspondiente a la cantidad mínima de pasos a realizar para ordenar el arreglo.
