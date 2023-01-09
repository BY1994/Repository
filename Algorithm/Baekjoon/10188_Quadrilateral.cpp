/*
10188 Quadrilateral

단순 구현 
*/

#include <stdio.h>

int main(void)
{
    int N, x, y;
    scanf("%d", &N);
    while (N--) {
        scanf("%d %d", &x, &y);
        for (int i = 0; i < y; ++i) {
            for (int j = 0; j < x; ++j) printf("X");
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
