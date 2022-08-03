/*
4889 �������� ���ڿ�

stack ���� 
�Ϲ������� ���� ���� ������ ���°� �ƴ϶�
���� ���� �ʴ� ��� �´� ������� �ٲ���� �Ѵ�.
* �Ǽ� ����Ʈ: �������� stack �� ���� ���� �׳� ���ϸ�
���̶�� �����ߴµ�, stack �� ���� ��ȣ�� ������ �����ִ�
���̹Ƿ� �ݸ� ���� ��ȣ�� �ٲ��ָ� �ȴ�. 
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
