#include <stdio.h>

/*
printf�� �� printf("%d\n", &a); �̷��� �ּҰ��� ��� �ٶ���
��� TC�� ���� ���� ������ �־���. 

fail ����! 
*/

int TC, a, b, ans, num;

int main(void)
{
	scanf("%d", &TC);
	for (int tc = 0; tc < TC; tc++)
	{
		ans = 0; // �ʱ�ȭ 
		scanf("%d %d", &a, &b);
// num = b-a+1;
		num = b-a;
		// ���� ���ڸ����� ���鼭 %���� ���ϱ�
		for (int i = 0; i<30; i++)
		{
			for (int j = 0; j <= num; j++)
//			for (int j = 0; j < (num % (1 << (i+1))); j++)
			{
				ans |= (a+j)&(1<<i); 
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
