#include <stdio.h>

int tc, TC, numbers[101];

int main(void)
{
	scanf("%d", &TC);
	for (tc = 1; tc<=TC; tc++)
	{
		for (i = 0; i<=100; i++)
		{
			// %c로 받고 0x30 빼기 
			scanf("%1d", &numbers[i]);
		}
		printf("Case #%d: ", tc);
		// 가장 처음 만나는 숫자만큼 스택에 들어가야함
		
		printf("\n");
	}
	return 0;
}
