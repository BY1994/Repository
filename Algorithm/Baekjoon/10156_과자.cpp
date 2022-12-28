/*
10156 과자

수학 사칙연산 
*/
#include <stdio.h>

int main(void)
{
    int K, N, M;
    scanf("%d %d %d", &K, &N, &M);
    if (K*N <= M) printf("0\n");
    else printf("%d\n", (K*N) - M);

    return 0;
}
