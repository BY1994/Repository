/*
2812 ũ�� �����

stack ����
�ε��� ���ٿ��� ������ ������ ������ �;��µ�
&& �� || �� short circuit �̶�� �Ѵ�.
�ƽ�Ű�ڵ�� '0' < '1' �̷� ���̴ϱ� ���� ���� ��ȯ���� �ʰ�
���ڿ��� ����Ͽ���.

Ʋ�Ƚ��ϴ�
�ݷ�
https://www.acmicpc.net/board/view/93032
10 4
7898111101
�� : 981111

10 4
7898111102
�� : 981112
==>
stack[sp] = 0 �� stack[sp-K] = 0 �� ����� ��� 
�������� K �� ���� ��� ������ �����ִ� ���� 

2022.07.30 ��� 
*/
#include <stdio.h>
 
int N, K;
char number[500010];
char stack[500010];
int sp;
int main(void)
{
	scanf("%d %d", &N, &K);
	scanf("%s", number);
	for (int i = 0; number[i]; ++i) {
		while (sp > 0 && K > 0 && stack[sp-1] < number[i]) {
			sp--;
			K--;
		}
		stack[sp++] = number[i];
	}
	stack[sp-K] = 0;
	printf("%s\n", stack);
	return 0;
}
