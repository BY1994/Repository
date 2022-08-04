/*
15815 õ�� ������ ����

����ǥ���� ����
stack

���� �Խñ��� ���ٰ� �ǹ��� ���� �ʾҴ� ���� ���޾Ҵ�
���ڰ� ���ڸ����� ������ ������
https://www.acmicpc.net/board/view/74635
 
�ݷ� �����
���� ǥ������ ������� �ʰ�, ���� ������ �´� �ڵ� 
(�� ���� �� ���ڸ� stack ����, �����ڴ� queue �� ������) 
https://www.acmicpc.net/board/view/70954
https://www.acmicpc.net/board/view/94263 
�Է�) 123*+4+
����) 11 

2022.08.04 ��� 
*/
#include <stdio.h>

int stack[110];
int sp;
char formula[110];

int main(void)
{
    scanf("%s", formula);
    for (int i = 0; formula[i]; ++i) {
        if (formula[i] == '+') {
            stack[sp-2] = stack[sp-2] + stack[sp-1];
            sp--;
        }
        else if (formula[i] == '-') {
            stack[sp-2] = stack[sp-2] - stack[sp-1];
            sp--;
        }
        else if (formula[i] == '*') {
            stack[sp-2] = stack[sp-2] * stack[sp-1];
            sp--;
        }
        else if (formula[i] == '/') {
            stack[sp-2] = stack[sp-2] / stack[sp-1];
            sp--;
        } else {
            stack[sp++] = formula[i] - '0';
        }
    }
    printf("%d\n", stack[0]);
    return 0;
}
