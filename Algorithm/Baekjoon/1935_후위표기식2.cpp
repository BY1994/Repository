/*
1935 후위 표기식 2

질문게시판 반례 만들기 
https://www.acmicpc.net/board/view/93300
3
AB+C-B*
5
4
1
정답 32.00
코드에서 A, B, C 값 입력 받을 때 마지막 값으로 덮어쓰는 문제가 있었음 

https://www.acmicpc.net/board/view/68720
4
AC+B+C+A+D+
1
2
3
4
정답 14.00
문제에서 입력되는 알파벳이 무조건 A, B, C 고 한 번씩만 들어온다고 간주하는 코드라 문제 발생
위의 코드는 반례 입력시 Type Error 가 발생한다. 
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
