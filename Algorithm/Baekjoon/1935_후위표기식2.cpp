/*
1935 ���� ǥ��� 2

�����Խ��� �ݷ� ����� 
https://www.acmicpc.net/board/view/93300
3
AB+C-B*
5
4
1
���� 32.00
�ڵ忡�� A, B, C �� �Է� ���� �� ������ ������ ����� ������ �־��� 

https://www.acmicpc.net/board/view/68720
4
AC+B+C+A+D+
1
2
3
4
���� 14.00
�������� �ԷµǴ� ���ĺ��� ������ A, B, C �� �� ������ ���´ٰ� �����ϴ� �ڵ�� ���� �߻�
���� �ڵ�� �ݷ� �Է½� Type Error �� �߻��Ѵ�. 
*/

#include <stdio.h>

int N;
char Formula[105];
int alphabet[100];
double stack[105];
int sp;

int main(void)
{
	scanf("%d", &N);
	scanf("%s", Formula);
	for (int i = 0; i < N; ++i)
		scanf("%d", &alphabet['A'+i]);
	
	for (int i = 0; Formula[i]; ++i) {
		if ('A' <= Formula[i] && Formula[i] <= 'Z') {
			stack[sp++] = alphabet[Formula[i]];
		}
		else if (Formula[i] == '*') {
			stack[sp-2] = stack[sp-2] * stack[sp-1];
			sp -= 1;
		}
		else if (Formula[i] == '/') {
			stack[sp-2] = stack[sp-2] / stack[sp-1];
			sp -= 1;
		}
		else if (Formula[i] == '+') {
			stack[sp-2] = stack[sp-2] + stack[sp-1];
			sp -= 1;
		}
		else if (Formula[i] == '-') {
			stack[sp-2] = stack[sp-2] - stack[sp-1];
			sp -= 1;
		}
	}
	
	printf("%.2lf\n", stack[0]);
	
	return 0;
}
