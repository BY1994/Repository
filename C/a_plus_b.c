#include <stdio.h>
int main(){
	int N;
	int a, b;
	int i;
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a+b);
	}
	return 0;
} 
