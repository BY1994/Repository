/*
1439 ������

�׸��� 
ans++; �� ���� �ű�� �������� -1 �ϰ� ¥��
��������� �ʴ�... ������ ans++; �� �ؿ� ��������
while �� ������ if (start <= end) �� �ٽ� Ȯ���ؾ��ؼ�
�װ� �����ϱ� ���� �̷��� �����Ͽ���. 
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

