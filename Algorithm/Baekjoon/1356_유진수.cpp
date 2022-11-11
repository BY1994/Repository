/*
1356 유진수 

N 은 최대 2147483647 이므로,
최대 10자리의 수가 들어온다.
최대로 가능한 크기는 9 를 9번 곱했다고 가정하면,  
387420489 이다.
처음 생각한 풀이는 (0 으로 나눠지는 경우가 있어서 런타임 에러 발생)
9 를 10번 곱해야했기 때문에 long long 으로 잡았지만
최종 통과 버전은 long long 으로 잡을 필요가 없었다. 
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
	char N[11];
	int len;
	int flag = 0;
	long long front, rear;

	scanf("%s", N);
	len = strlen(N);
	
	for (int i = 0; i < len; i++) {
		N[i] -= '0';
	}
	
	// i 가 기준선 
	for (int i = 0; i < len-1; i++) {
		front = rear = 1;
		
		for (int d1 = 0; d1 <= i; d1++) {
			front *= N[d1];
		}
		for (int d2 = i+1; d2 < len; d2++) {
			rear *= N[d2];
		}
		if (front == rear) {
			flag = 1;
			break;
		}
	}
	
	if (flag) printf("YES\n");
	else printf("NO\n");

	return 0;
}

// Division By Zero 에러 발생
// 0 이 나오지 않는다는 보장이 문제에 없다.
#if 0 
#include <stdio.h>
#include <string.h>

int main(void)
{
	char N[11];
	int len;
	int flag = 0;
	long long front = 1;
	long long rear = 1;

	scanf("%s", N);
	len = strlen(N);
	
	for (int i = 0; i < len; i++) {
		N[i] -= '0';
		rear *= N[i];
	}
	
	for (int i = 0; i < len-1; i++) {
		front *= N[i];
		rear /= N[i];
		if (front == rear) {
			flag = 1;
			break;
		}
	}

	if (flag) printf("YES\n");
	else printf("NO\n");

	return 0;
}
#endif
