/*
1996 지뢰 찾기 

구현 
*/

#include <stdio.h>

char map[1001][1001];
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int main(void)
{
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        scanf("%s", map[i]);
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (map[i][j] != '.') printf("*");
            else {
                int cnt = 0;
                for (int d = 0; d < 8; ++d) {
                    int nx = i + dx[d];
                    int ny = j + dy[d];
                    if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                    if (map[nx][ny] != '.') cnt += map[nx][ny] - '0';
                }
                if (cnt >= 10) printf("M");
                else printf("%d", cnt);
            }
        }
        printf("\n");
    }
    return 0;
}
