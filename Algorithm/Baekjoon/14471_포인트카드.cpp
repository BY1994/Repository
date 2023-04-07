/*
14471 포인트 카드

그리디

M-1 개 이상의 경품을 가진다는 조건이 있어서
정렬 문제가 아니라 그리디 문제가 됨!!
이 부분이 신기했다. 
*/
#include <stdio.h>
#define max(a, b) ((a) > (b))? (a) : (b)

int main(void)
{
    int N, M, A, B, need;
    int total = 0, m = 0;
    scanf("%d %d", &N, &M);
    while (M--) {
        scanf("%d %d", &A, &B);
        need = max(N-A, 0);
        total += need;
        m = max(need, m);
    }
    printf("%d\n", total - m);

    return 0;
}
