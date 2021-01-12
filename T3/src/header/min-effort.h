/*
 * Function:	int max.
 * Parameters:	int* A: 	 arreglo de entrada.
 * 				int n:  	 tamaño de A.
 * Return:		int maximum: mayor numero de A.
 * Description:	calcula el maximo numero de A.
 */
int max(int* A, int n);
/*
 * Function:	int lis.
 * Parameters:	int* A: arreglo de entrada.
 * 				int n:  largo de A.
 * Return:		int m:  tamaño de la mayor subsequencia
 * 					    creciente de A.
 * Description:	calcula el largo de la mayor subsequencia
 * 				creciente de A.
 */
int lis (int* A, int n);
/*
 * Function:	int minEffort.
 * Parameters:	int* A: arreglo de entrada.
 * 				int n:  largo de A.
 * Return:		int m:  numero de pasos para ordenar A.
 * Description:	calcula la menor cantidad de pasos para
 * 				ordenar A.
 */
int minEffort (int* A, int n);
