#include <stdio.h>

int tc, TC, numbers[101];

int main(void)
{
	scanf("%d", &TC);
	for (tc = 1; tc<=TC; tc++)
	{
		for (i = 0; i<=100; i++)
		{
			// %c�� �ް� 0x30 ���� 
			scanf("%1d", &numbers[i]);
		}
		printf("Case #%d: ", tc);
		// ���� ó�� ������ ���ڸ�ŭ ���ÿ� ������
		
		printf("\n");
	}
	return 0;
}
