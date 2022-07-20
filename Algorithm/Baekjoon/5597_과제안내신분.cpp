/*
5597 과제 안 내신 분..?

기초 비트 연습
30 명 중 28 명이 제출하였을 때, 제출 안 한 2명 출력하기 
*/

#include <stdio.h>

int main()
{
    int n;
    unsigned int check = 0;
    for (int i = 0; i < 28; ++i) {
        scanf("%d", &n);
        check |= (1 << (n-1));
    }

    for (int i = 0; i < 30; ++i) {
        if ((check & 1) == 0) {
            printf("%d\n", i+1);
        }
        check >>= 1;
    }

    return 0;
}
