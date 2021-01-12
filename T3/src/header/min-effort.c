#include "min-effort.h"
#include <limits.h>

int max (int* A, int n) {
	int maximum = INT_MIN;
	for (int i=0; i<n; i++)
		if (A[i] > maximum)
			maximum = A[i];
	return maximum;
}

int lis (int* A, int n) {
	int lis[n];
	int m;
	lis[0] = 1;

	for (int i=1; i<n; i++) {
		lis[i] = 1;
		for (int j=0; j<i; j++)
			if (A[i] >= A[j] && lis[i] <= lis[j]+1)
				lis[i] = lis[j] + 1;
	}
	m = max(lis,n);
	return m;
}

int minEffort (int* A, int n) {
	int m = n-lis(A,n);
	return m;
}
