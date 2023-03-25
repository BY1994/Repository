/*
2588 곱셈 

곱셈 중간 결과와 최종 결과 출력하기
무조건 3자리 * 3자리이기 때문에
간단하게 계산 가능 

브론즈 3 문제 중 쉬운 편 
*/

#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    printf("%d\n", a*(b%10));
    printf("%d\n", a*((b/10)%10));
    printf("%d\n", a*((b/100)%10));
    printf("%d\n", a*b);
    return 0;
}
