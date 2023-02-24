/*
16693 Pizza Deal 

기하학, 사칙연산
면적과 가격 vs. 반지름과 가격이 주어졌을 때 더 이득인 피자 고르기
A1 / P1
R1 * R1 * 3.14 / P2
중 더 큰 걸 찾는 거니까 둘다 P1*P2 를 곱해주었다.
그래서 아래 코드의 식이 나옴 

3.14 는 JPL 에서 행성간 항법을 계산할 때 사용한다는 값까지 사용했다.
(이걸 작게 사용하면 틀리는 저격 데이터들이 있다)
 https://kids.donga.com/mobile/?ptype=article&no=20190314154822649351
*/

#include <stdio.h>

int main(void)
{
    double A1, P1, R1, P2;
    scanf("%lf %lf", &A1, &P1);
    scanf("%lf %lf", &R1, &P2);
    
    if (A1 * P2 > R1 * R1 * 3.141592653589793 * P1)
        printf("Slice of pizza\n");
    else printf("Whole pizza\n");

    return 0;
}
