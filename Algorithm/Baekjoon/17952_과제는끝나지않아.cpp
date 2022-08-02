/*
17952 과제는 끝나지 않아!

스택 
stack 사이즈 잡게 잡아서 시간초과 한 번 남 (문제 잘못 이해)
원래는 런타임 에러가 나야하는데, 버퍼가 있었나보다. 
*/

#include <stdio.h>

int N, ans;
struct homework {
    int score;
    int remain;
}stack[1000001];
int sp;

int main(void)
{
    int val, score, remain;
    scanf("%d", &N);
    while (N--) {
        scanf("%d", &val);
        if (val) {
            scanf("%d %d", &score, &remain);
            if (--remain)
                stack[sp++] = {score, remain};
            else
                ans += score;
        } else if (sp > 0) {
            if (--stack[sp-1].remain == 0) {
                ans += stack[sp-1].score;
                sp--;
            }
        }
    }
    printf("%d\n", ans);
    return 0;
}
