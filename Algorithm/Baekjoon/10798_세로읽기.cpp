/*
10798 �����б�

����, ���ڿ� 
�ٸ� ���� ���̵��� ���� ����� 1 �� ��������� ���� å���� �� �ƴѰ� �ʹ�. 
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
