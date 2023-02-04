/*
10707 수도요금 

수학 사칙연산 
*/

#include <stdio.h>

int main(void)
{
    int X, Y, A, B, C, D, P;
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);
    scanf("%d", &D);
    scanf("%d", &P);
    
    X = A*P;
    Y = B;
    if (P > C) Y += (P-C) * D;
    if (X > Y) printf("%d\n", Y);
    else printf("%d\n", X);

    return 0;
}
