#include<stdio.h>
int main(){
	int N;
	int res = 1; // �̰� ó���� 0���� �ʱ�ȭ�ߴٰ� ���� �� 0�� �Ǿ���.  
	int i; 
	scanf("%d", &N);
	for (i=0; i<N; i++){
		res *= (i+1);
	}
	printf("%d", res);
	return 0;
}
