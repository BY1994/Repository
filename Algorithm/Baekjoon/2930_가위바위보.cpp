/*
2930 가위 바위 보
 
구현, 그리디, 브루트 포스

룩업테이블 이용해서 모든 경우 점수 다 계산해서 최고점 구함 
*/

#include <stdio.h>

char score[128][128];
char my[51];
char friends[51][51];

void init(void) {
    score['S']['P'] = 2;
    score['S']['S'] = 1;
    score['P']['R'] = 2;
    score['P']['P'] = 1;
    score['R']['S'] = 2;
    score['R']['R'] = 1;
}

int max(int a, int b) {
    return (a > b)? a:b;
}
int main(void)
{
    int N, R, maxans = 0, curans = 0;
    init();
    scanf("%d", &R);
    scanf("%s", my);
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        scanf("%s", friends[i]);
    }
    for (int i = 0; i < R; ++i) {
        int s = 0, p = 0, r = 0;
        for (int j = 0; j < N; ++j) {
            s += score['S'][friends[j][i]];
            p += score['P'][friends[j][i]];
            r += score['R'][friends[j][i]];
            curans += score[my[i]][friends[j][i]];
        }
        maxans += max(s, max(p, r));
    }
    printf("%d\n", curans);
    printf("%d\n", maxans);
    return 0;
}
