/*
1075 나누기

brute force
마지막 끝에 2자리를 완전탐색하면 되므로
100 개만 돌면 된다! 
(2,000,000,000 번 돌 필요 없다)
https://www.acmicpc.net/board/view/17326

하지만 그렇게 안 풀고 가장 가까운 배수에 원래 값 한 번 더해주면
구할 수 있을 것 같아서 수학으로 풀었다. 
*/

#include <stdio.h>

int main(void)
{
    long long N, F;
    scanf("%lld", &N);
    scanf("%lld", &F);
    
    N -= N % 100;
    if (N % F)
        printf("%02lld\n", ((N/F)*F + F) % 100);
    else
        printf("00\n");

    return 0;
}
