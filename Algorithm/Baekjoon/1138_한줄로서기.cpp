/*
1138 한 줄로 서기 

구현
재밌었던 문제 
*/

#include <stdio.h>
int ans[11];

int main(void)
{
    int N; int bigger;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        scanf("%d", &bigger);
        for (int j = 0; j < N; ++j) {
            if (ans[j]) continue;
            if (bigger == 0) {
                ans[j] = i+1;
                break;
            }
            bigger--;
        }
    }
    for (int i = 0; i < N; ++i) printf("%d ", ans[i]);
    printf("\n");

    return 0;
}
