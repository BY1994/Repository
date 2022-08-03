/*
4889 안정적인 문자열

stack 응용 
일반적으로 열고 닫은 개수만 세는게 아니라
쌍이 맞지 않는 경우 맞는 모양으로 바꿔줘야 한다.
* 실수 포인트: 마지막에 stack 에 남은 값을 그냥 더하면
답이라고 생각했는데, stack 에 열린 괄호의 개수만 남아있는
것이므로 반만 닫힌 괄호로 바꿔주면 된다. 
*/

#include <stdio.h>
int stack;
int ret;
char S[2001];

int main(void)
{
	for (int tc = 1; ; tc++) {
		scanf("%s", S);	
		if (S[0] == '-') break;
		stack = 0;
		ret = 0;
		for (int i = 0; S[i]; ++i) {
			if (S[i] == '{') {
				stack++;
			} else {
				if (stack > 0)
					stack--;
				else {
					stack++;
					ret++;					
				}
			}
		}
		ret += stack/2;
		printf("%d. %d\n", tc, ret);
	}

	return 0;
}
