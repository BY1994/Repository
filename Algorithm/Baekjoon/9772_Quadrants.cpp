/*
9772 Quadrants

���и� Ȯ��
0, 0 �� ��쵵 AXIS ����ؾ��� 
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
