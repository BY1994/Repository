#include <stdio.h>

int main(){
	int T;
	int t=0;
	// input
	scanf("%d", &T); 
	printf("Hello World!\n");
	printf("%d\n", T);
	
	// int t=0; 을 하면 실행이 안 됨 
	for (t=0; t<T; t++)
	{
		int N, K;
		scanf("%d %d", &N, &K);
		int drives[N];
		int blocks[K];
		int i=0 ,j = 0;
		
		for (i=0; i<N; i++)
		{
			scanf("%d", &drives[i]);
		}
		printf("실행 여부\n");
		for (j=0; j<K; j++)
		{
			scanf("%d", &blocks[j]);
		}
		printf("반복\n");
	}
	return 0;
}
