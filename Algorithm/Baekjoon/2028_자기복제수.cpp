/*
2028 자기복제수

제곱했을 때 맨 뒷자리에 자기 자신이 나타나면
자기복제수로 판단 

1등 풀이에 비해 필요없는 코드가 많음 
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

// 1등 풀이 비교
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
