/*
1918 ���� ǥ��� 

dfs �� Ǯ� ������,
������ ���� ¥�� Ǯ��� ���� 

�ݷ�
https://www.acmicpc.net/board/view/76519
A*B-C*D/E
��: AB*CD*E/- 

https://www.acmicpc.net/board/view/88165
((A+B)*C)/D
��: AB+C*D/ 

���� ���� ������ ����
A+B*(C+D*E-A+C+B*D)-A+B 
��: ABCDE*+A-C+BD*+*+A-B+ 

���� ��ȣ�� �ݴ� ��ȣ ó���� ��� �ؾ��ϳ� ����ߴµ�,
�ٸ� �� Ǯ�̸� ���� �� ��ȣ�� stack �� �־������ �ȴ�. 
https://donggoolosori.github.io/2020/10/19/boj-1918/
*/

#include <stdio.h>

char Formula[101];
char stack[101];
char ans[101];
int index;
int sp;
int priority[50];

int main(void)
{
	priority['+'] = priority['-'] = 1;
	priority['*'] = priority['/'] = 2;
	scanf("%s", Formula);
	for (int i = 0; Formula[i]; ++i) {
		if (Formula[i] >= 'A' && Formula[i] <= 'Z') {
			ans[index++] = Formula[i];
		}
		else { 
			if (Formula[i] == '(') {
				stack[sp++] = Formula[i];
			}
			else if (Formula[i] == ')') {
				while (stack[sp-1] != '(')
					ans[index++] = stack[--sp];
				sp--;
			}
			else if (sp == 0 || (sp > 0 && stack[sp-1] == '('))
				stack[sp++] = Formula[i];
			else {
				while (sp > 0 && stack[sp-1] != '(' && priority[stack[sp-1]] >= priority[Formula[i]]) {
					ans[index++] = stack[--sp];
				}
				stack[sp++] = Formula[i];
			}
		}
	}

	while (sp > 0)
		ans[index++] = stack[--sp];

	ans[index] = 0;
	printf("%s\n", ans);
	return 0;
}

// ��ȣ�� ������ ��� �����ϴ� ù �õ�
/* 
#include <stdio.h>

char Formula[101];
char stack[101];
char ans[101];
int index;
int sp;
int priority[50];

int main(void)
{
	priority['+'] = priority['-'] = 1;
	priority['*'] = priority['/'] = 2;
	scanf("%s", Formula);
	for (int i = 0; Formula[i]; ++i) {
		if (Formula[i] >= 'A' && Formula[i] <= 'Z') {
			ans[index++] = Formula[i];
		}
		else { 
			if (sp == 0)			
				stack[sp++] = Formula[i];
			else if (Formula[i] == '(') {
				ans[index++] = Formula[i+1];
				stack[sp++] = Formula[i+2];
				i += 2;
			}
			else if (Formula[i] == ')') {
				ans[index++] = stack[--sp];
			}
			else if (Formula[i+1] == '(') {
				stack[sp++] = Formula[i];
			} 
			else if (priority[stack[sp-1]] >= priority[Formula[i]]) {
				ans[index++] = stack[--sp];
				//stack[sp++] = Formula[i];
			}
			else if (priority[stack[sp-1]] < priority[Formula[i]]){
				//stack[sp++] = Formula[i]; // *( �� ��� ������ �ϴ� stack �� �ֱ� 
				ans[index++] = Formula[i+1];
				ans[index++] = Formula[i];
				i += 1;
			}
		}
	}
	for (int i = 0; i < sp; ++i) {
		ans[index++] = stack[i];
	}
	ans[index] = 0;
	printf("%s\n", ans);
	return 0;
}
*/
