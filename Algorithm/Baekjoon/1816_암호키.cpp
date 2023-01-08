/*
1816 ��ȣ Ű 

���� / ���Ʈ���� �˰��� / ������ 

��� ���μ��� 10^6���� Ŀ���Ѵٴ� ��
�ϳ��� ���� �� ������ Ʋ�ȴٴ� ��! 
*/

#include <stdio.h>

int prime[1000001];

int main(void)
{
	int N;
	unsigned long long S;
	// 1. �Ҽ� ���ϱ�
	for (int i = 2; i <= 1000; ++i) {
		for (int j = 2; j <= 1000; ++j) {
			prime[i*j] = 1;
		}
	} 
	// 2. ���μ� ��� 
	scanf("%d", &N);
	for (int n = 0; n < N; ++n) {
		int flag = 0;
		scanf("%llu", &S);
		for (int i = 2; i <= 1000000; ++i) {
			if (!prime[i] && !(S % i)) {
				flag = 1;
				break;
			}
		}
		if (flag) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
} 


// prime �� ���� �����ϸ� �ð��� �ξ� ����� 
#if 0
#include <stdio.h>

char p[1000001];
int idx, prime[78498];

void init(){
	int i, j;
	p[0]=p[1]=1;
	for(i=2; i<=1000; ++i){
		if(!p[i]){
			prime[idx++]=i;
			for(j=i+i; j<=1000000; j+=i){
				p[j]=1;
			}
		}
	}
	for(; i<=1000000; ++i){
		if(!p[i]){
			prime[idx++]=i;
		}
	}
}

int main(void){
	int i, N, flag;
	long long S;

	scanf("%d", &N);
	init();
	while(N--){
		scanf("%lld", &S);
		flag=0;
		for(i=0; i<idx; ++i){
			if(S%prime[i]==0){
				flag=1;
				break;
			}
		}
		printf("%s\n", (flag)?"NO":"YES");
	}

	return 0;
}
#endif
