#include <stdio.h>

int main(){
	int T;
	int t=0;
	// input
	scanf("%d", &T); 
	printf("Hello World!\n");
	printf("%d\n", T);
	
	// int t=0; �� �ϸ� ������ �� �� 
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
		printf("���� ����\n");
		for (j=0; j<K; j++)
		{
			scanf("%d", &blocks[j]);
		}
		printf("�ݺ�\n");
	}
	return 0;
}
