/*
12605 �ܾ���� ������ 

stack �� �ܾ ��°�� ���� ����� ���
�������� ������ �����ߴ�.

input �� ���� �� ' ' ������ ������ %s �� �ű⼭ ���ܹ�����
�������� '\n' �� ���� ������ �޵��� �ϴ� ����� ã�Ҵ�.
" %[^\n]" �տ� ���⸦ �� �ϸ� ���� ���� �Է� ���� �� ����. 
https://clgnsdl94.tistory.com/m/24 

�ٸ� Ǯ��
(1) ����ϰ� stack �� �ε����� �����ϴ� ���
https://www.acmicpc.net/source/7564505
(2) stack �� 2���� �迭�� �ؼ� �ƿ� ���ڸ� �� �ִ� ���
*/
#include <stdio.h>

int N;
char sentence[51];
int sp;
int stack[101];

int main(void)
{
    scanf("%d", &N);
    for (int tc = 1; tc <= N; tc++) {
        int i;
        printf("Case #%d:", tc);
        sp = 0;
        scanf(" %[^\n]", sentence);
        stack[sp++] = 0;
        for (i = 0; sentence[i]; ++i) {
            if (sentence[i] == ' ') {
                stack[sp++] = i;
                stack[sp++] = i+1;
            }
        }
        stack[sp] = i;
        while (sp > 0) {
            printf(" ");
            for (i = stack[sp-1]; i < stack[sp]; ++i) {
                printf("%c", sentence[i]);
            }
            sp -= 2;
        }
        printf("\n");
    }
}
