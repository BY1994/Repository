/*
1225 이상한 곱셈

만자리의 수이기 때문에 char 로 받아야함
A: 9 가 만개, B: 9가 만개면
81 * 만 개 * 만개 이므로 81억이고, long long 안에 들어옴 
*/

#include <stdio.h>

char A[10001];
char B[10001];

int main()
{
    unsigned long long ans = 0;
    scanf("%s %s", A, B);
    for (int i = 0; A[i]; i++) {
        for (int j = 0; B[j]; j++) {
            ans += (A[i] - '0') * (B[j] - '0');
        }
    }
    printf("%llu\n", ans);

    return 0;
}
