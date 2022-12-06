/*
2160 그림 비교 

반례: 완전히 다른 경우를 대비해서 초기화가 필요함
이거 때문에 한 번 틀림 
https://www.acmicpc.net/board/view/75825
Input:
2
.......
.......
.......
.......
.......
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX

Output:
1 2

4 중 포문을 쓰지 않으려면
35 개 값이므로 0과 1로 변환해서
unsigned long long 에 bit 로 넣으면
xor 연산으로 빠르게 찾을 수 있을 것 같다. 
*/

#include <stdio.h>

char figure[51][5][8];

int main(void)
{
    int N;
    scanf("%d", &N);
    for (int n = 1; n <= N; ++n) {
        for (int i = 0; i < 5; ++i) {
            scanf("%s", figure[n][i]);
        }
    }
    
    int min = 35;
    int ans[2] = {1, 2};
    for (int first = 1; first <= N; ++first) {
        for (int second = first + 1; second <= N; ++second) {
            int diff = 0;
            for (int i = 0; i < 5; ++i) {
                for (int j = 0; j < 7; ++j) {
                    if (figure[first][i][j] != figure[second][i][j])
                        diff++;
                }
                if (min < diff) break;
            }
            if (min > diff) {
                min = diff;
                ans[0] = first;
                ans[1] = second;
            }
        }
    }
    printf("%d %d\n", ans[0], ans[1]);

    return 0;
}
