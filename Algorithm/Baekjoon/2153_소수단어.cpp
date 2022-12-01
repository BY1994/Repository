/*
2153 소수 단어

수학
소수 판정은 작은수부터 나눠보는 거로 했다.
작은수일 수록 나눠지는 수일 확률이 높을 테니까
for 문을 상대적으로 덜 돌거라고 생각했다. 
*/

#include <stdio.h>

char dict[128];
char word[21];

void init(void) {
    for (int i = 1; i <= 26; ++i) {
        dict[i+'a'-1] = i;
        dict[i+'A'-1] = i+26;
    }
}

int main(void)
{
    int N = 0;
    int flag = 0;

    init();
    scanf("%s", word);
    for (int i = 0; word[i]; ++i) {
        N += dict[word[i]];
    }
    for (int i = 2; i < N; ++i) {
        if (N % i == 0) {
            flag = 1;
            break;
        }
    }
    if (flag) printf("It is not a prime word.\n");
    else printf("It is a prime word.\n");

    return 0;
}
