/*
17413 단어 뒤집기 2

stack
띄어쓰기 있는 입력 받는 법
https://github.com/BY1994/Repository/blob/9e90315dbd3b068eda197b9e38c3f5bcfae3450e/Algorithm/Baekjoon/12605_%EB%8B%A8%EC%96%B4%EC%88%9C%EC%84%9C%EB%92%A4%EC%A7%91%EA%B8%B0.cpp

시간 1등 풀이
굳이 stack 안 쓰고, 조건에 따라 swap 만 사용
https://www.acmicpc.net/source/35428134

2022.08.05 통과 
*/

#include <stdio.h>
char S[100010];
char stack[100010];
int sp;

int main(void)
{
	int index = 0;
	scanf(" %[^\n]", S);
	while (S[index]) {
		if (S[index] == '<') {
			while (sp > 0) printf("%c", stack[--sp]);
			while (S[index] != '>') printf("%c", S[index++]);
			printf(">");
		}
		else if (S[index] == ' ') {
			while (sp > 0) printf("%c", stack[--sp]);
			printf(" ");
		}
		else {
			stack[sp++] = S[index];
		}
		index++;
	}
	while (sp > 0) printf("%c", stack[--sp]);
	printf("\n");
	return 0;
}
