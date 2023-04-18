/*
22864 피로도

그리디, 시뮬레이션
B 최대값은 10,000 인데 24시간 다 일해도 240,000 이므로
int 범위를 넘지 않는다. 
*/

#include <stdio.h>
int main(void)
{
    int A, B, C, M;
    int tired = 0, output = 0;
    scanf("%d %d %d %d", &A, &B, &C, &M);
    for (int h = 0; h < 24; ++h) {
        if (tired + A > M) {
            tired -= C;
            if (tired < 0)
                tired = 0;
        } else {
            tired += A;
            output += B;
        }
    }
    printf("%d\n", output);
    return 0;
}
