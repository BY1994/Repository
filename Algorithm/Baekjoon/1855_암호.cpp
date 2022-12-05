/*
1855 ��ȣ

�迭 �� ���� �ε��������� �Ϸ��� �ߴµ�,
�����ؼ� �׳� �迭�� ���� 

��, ���� �򰥸��µ� ���� �Ẹ�� �� �򰥸���.
a e i j f b c g k l h d
=>
a e i
b f j
c g k
d h l 
=>
a b c d e f g h i j k l
*/

#include <stdio.h>
#include <string.h>

char board[201][21];
char string [201];

int main(void)
{
    int N, M;
    int s = 0;
    scanf("%d", &N);
    scanf("%s", string);
    M = strlen(string)/N;
    for (int i = 0; i < M; i += 2) {
        for (int j = 0; j < N; ++j) {
            board[i][j] = string[s++];
        }
        for (int j = N-1; j >= 0; --j) {
            board[i+1][j] = string[s++];
        }
    }
    
    for (int j = 0; j < N; ++j) {
        for (int i = 0; i < M; ++i) {
            printf("%c", board[i][j]);
        }
    }
    printf("\n");
    return 0;
}
