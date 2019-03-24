#include<stdio.h>
int main(){
	int N;
	int res = 1; // 이걸 처음에 0으로 초기화했다가 답이 다 0이 되었다.  
	int i; 
	scanf("%d", &N);
	for (i=0; i<N; i++){
		res *= (i+1);
	}
	printf("%d", res);
	return 0;
}
