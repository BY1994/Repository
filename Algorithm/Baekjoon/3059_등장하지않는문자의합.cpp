/*
3059 등장하지 않는 문자의 합 

구현, 문자열, 비트연산
원래 문제 분류에 비트연산은 없었지만, 알파벳 26글자만 고려하면 되기 때문에
비트 연산이 구현하기에 더 편리할 것 같아 비트 연산으로 구현하였다. 
*/

#include <stdio.h>

char S[1001];

int main(void)
{
    int T;
    scanf("%d", &T);
    while (T--) {
        int count = 0; int ans = 0;
        scanf("%s", S);
        for (int i = 0; S[i]; ++i) {
            count |= 1 << (S[i]-'A');
        }
        for (int i = 0; i < 26; ++i) {
            if ((count >> i) & 1) continue;
            ans += 'A' + i;
        }
        printf("%d\n", ans);
    }

    return 0;
}
