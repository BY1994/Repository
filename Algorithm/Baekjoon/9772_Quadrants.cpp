/*
9772 Quadrants

사사분면 확인
0, 0 인 경우도 AXIS 출력해야함 
*/

#include <stdio.h>

int main(void)
{
    float x, y;
    while (1) {
        scanf("%f %f", &x, &y);
        if (x > 0.0 && y > 0.0) printf("Q1\n");
        else if (x < 0.0 && y > 0.0) printf("Q2\n");
        else if (x < 0.0 && y < 0.0) printf("Q3\n");
        else if (x > 0.0 && y < 0.0) printf("Q4\n");
        else printf("AXIS\n");

        if (x == 0.0 && y == 0.0) break;

    }

    return 0;
}
