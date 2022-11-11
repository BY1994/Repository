/*
1356 ������ 

N �� �ִ� 2147483647 �̹Ƿ�,
�ִ� 10�ڸ��� ���� ���´�.
�ִ�� ������ ũ��� 9 �� 9�� ���ߴٰ� �����ϸ�,  
387420489 �̴�.
ó�� ������ Ǯ�̴� (0 ���� �������� ��찡 �־ ��Ÿ�� ���� �߻�)
9 �� 10�� ���ؾ��߱� ������ long long ���� �������
���� ��� ������ long long ���� ���� �ʿ䰡 ������. 
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
	
	// i �� ���ؼ� 
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

// Division By Zero ���� �߻�
// 0 �� ������ �ʴ´ٴ� ������ ������ ����.
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
