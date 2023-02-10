/*
5598 카이사르 암호

구현 
*/
#include <stdio.h>

char Cdict[128];
char str[1001];

void init(void) {
    for (int i = 0; i < 26; ++i) {
        Cdict[(i+3)% 26 + 'A'] = i + 'A';
    }
}

int main(void)
{
    init();
    scanf("%s", str);
    for (int i = 0; str[i]; ++i) {
        printf("%c", Cdict[str[i]]);
    }
    printf("\n");

    return 0;
}
