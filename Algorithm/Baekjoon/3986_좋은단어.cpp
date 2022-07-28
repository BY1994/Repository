/*
3986 좋은 단어

스택 기초
*/

#include <stdio.h>

int N;
char S[100010];
int stack[100010];
int sp;

int check(void)
{
    sp = 0;
    stack[sp++] = S[0];
    for (int j = 1; S[j]; ++j) {
        if (stack[sp-1] == S[j]) {
            sp--;
        }
        else {
            stack[sp++] = S[j];
        }
    }
    if (sp > 0) return 0;
    return 1;
}

int main()
{
    int ans = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        scanf("%s", S);
        ans += check();
    }
    printf("%d\n", ans);

    return 0;
}