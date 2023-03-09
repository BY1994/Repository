/*
2774 아름다운 수

couting

X[i]-'0' 에서 -'0' 빼먹어서 예제 안 나왔었음...
*/

#include <stdio.h>
int T;
char X[12];

int main(void)
{
    scanf("%d", &T);
    while (T--) {
        int count[10] = {0};
        int beauty = 0;
        scanf("%s", X);
        for (int i = 0; X[i]; ++i) {
            count[X[i]-'0'] += 1;
        }
        for (int i = 0; i < 10; ++i) {
            beauty += !!count[i];
        }
        printf("%d\n", beauty);
    }

    return 0;
}
