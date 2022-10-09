/*
1769 3�� ��� 

1000000 �ڸ��� int ���� �ȿ� ������ ������
�װ� 9 * 100������ ����ϸ� �ٷ� int ���� �ȿ� ����
�׷��� ó�� ���� �� �ٷ� ���� 

�׷��� ó�� ���� ��ǲ�� �� �ڸ����� ��츦 ����Ͽ�
���� ó���� goto ������ ���� 
*/
#include <stdio.h>

char numbers[1000010];
int num;
int count;

int main(void)
{
	int i;

	// start
	scanf("%s", numbers);
	for (i = 0; numbers[i]; i++) {
		num += (int)(numbers[i] - '0');
	}
	if (i == 1)
		goto out;
	count++;
	
	// find ans
	while (num / 10) {
		int next = 0;
		while (num){
			next += num % 10;
			num /= 10;
		}
		num = next;
		count++;
	}
	
	// print
out:
	printf("%d\n", count);
	printf("%s\n", (num % 3)? "NO" : "YES");
	return 0;
}
