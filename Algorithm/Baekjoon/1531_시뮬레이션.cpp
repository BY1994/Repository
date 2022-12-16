/*
1531 투명 

시뮬레이션 
*/

#include <stdio.h>

int figure[101][101];

int main(void)
{
    int N, M, sx, sy, ex, ey;
    int ans = 0;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; ++i) {
        scanf("%d %d %d %d", &sx, &sy, &ex, &ey);
        for (int x = sx; x <= ex; ++x) {
            for (int y = sy; y <= ey; ++y) {
                figure[x][y]++;
            }
        }
    }
    for (int x = 1; x <= 100; ++x) {
        for (int y = 1; y <= 100; ++y) {
            if (figure[x][y] > M) ans++;
        }
    }
    printf("%d\n", ans);
    return 0;
}
