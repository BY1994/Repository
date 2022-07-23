/*
1918 후위 표기식 

dfs 로 풀어도 되지만,
로직을 직접 짜서 풀어보기 도전 

반례
https://www.acmicpc.net/board/view/76519
A*B-C*D/E
답: AB*CD*E/- 

https://www.acmicpc.net/board/view/88165
((A+B)*C)/D
답: AB+C*D/ 

내가 만든 복잡한 수식
A+B*(C+D*E-A+C+B*D)-A+B 
답: ABCDE*+A-C+BD*+*+A-B+ 

여는 괄호랑 닫는 괄호 처리를 어떻게 해야하나 고민했는데,
다른 분 풀이를 보니 그 괄호도 stack 에 넣어버리면 된다. 
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

// 괄호가 복잡한 경우 실패하는 첫 시도
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
				//stack[sp++] = Formula[i]; // *( 인 경우 때문에 일단 stack 에 넣기 
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
