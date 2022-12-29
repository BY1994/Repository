/*
10798 세로읽기

구현, 문자열 
다른 문제 난이도에 비해 브론즈 1 이 상대적으로 높게 책정된 것 아닌가 싶다. 
*/
#include <stdio.h>

char board[5][16];

int main(void)
{
    for (int i = 0; i < 5; ++i) scanf("%s", board[i]);
    for (int j = 0; j < 15; ++j) {
        for (int i = 0; i < 5; ++i) {
            if (board[i][j]) printf("%c", board[i][j]);
        }
    }
    printf("\n");
    return 0;
}
