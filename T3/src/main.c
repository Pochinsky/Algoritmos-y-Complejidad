#include <stdio.h>
#include <stdlib.h>
#include "./header/min-effort.h"

int main (int argc, char** argv) {
	if (argc == 2) {
		FILE* fp = fopen(argv[1],"r");
		if (fp == NULL) {
			printf("Archivo %s no se pudo abrir correctamente.\n",argv[1]);
			printf("Programa finalizado.\n");
			exit(1);
		}

		int n, min;
		while (fscanf(fp,"%d",&n) != EOF) {
			int A[n];
			for (int i=0; i<n; i++)
				fscanf(fp,"%d",(A+i));
			min = minEffort(A,n);
			printf("%d\n",min);
		}
	}
	else {
		printf("Argumentos de programa insuficientes.\n");
		printf("Programa finalizado.\n");
		return -1;
	}
}
