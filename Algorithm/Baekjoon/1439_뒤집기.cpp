/*
1439 뒤집기

그리디 
ans++; 을 위로 옮기고 마지막에 -1 하게 짜서
깔끔하지는 않다... 하지만 ans++; 을 밑에 넣으려면
while 의 조건인 if (start <= end) 를 다시 확인해야해서
그걸 방지하기 위해 이렇게 변경하였다. 
*/

#include <stdio.h>
#include <string.h>

char S[1000001];
int main(void)
{
	scanf("%s", S);
	int start = 0;
	int end = strlen(S)-1;
	int ans = 0;
	int current = S[0];
	while (start <= end) {
		ans++; 
		while (S[start] == current) start++;
		while (S[end] == current) end--;
		current = S[start];
	}
	printf("%d\n", ans-1);
	return 0;
}

