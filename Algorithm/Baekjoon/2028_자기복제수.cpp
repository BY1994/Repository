/*
2028 �ڱ⺹����

�������� �� �� ���ڸ��� �ڱ� �ڽ��� ��Ÿ����
�ڱ⺹������ �Ǵ� 

1�� Ǯ�̿� ���� �ʿ���� �ڵ尡 ���� 
*/

#include <stdio.h>

int len(int N) {
    int count = 0;
    while (N > 0) {
        N /= 10;
        count++;
    }
    return count;
}

int main(void)
{
    int T, N;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        int mod = 1;
        scanf("%d", &N);
        for (int j = 0; j < len(N); ++j) mod *= 10;
        if ((N*N) % mod == N) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

// 1�� Ǯ�� ��
/*
#include<cstdio>
int t,n,s,a;
int main(){
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        s=n*n;a=1;
        while(a<=n)a*=10;
        printf("%s\n",s%a==n?"YES":"NO");
    }
}
*/ 
