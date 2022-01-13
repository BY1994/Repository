#include <stdio.h>

/*
printf할 때 printf("%d\n", &a); 이렇게 주소값을 찍는 바람에
모든 TC가 같은 값이 나오고 있었다. 

fail 상태! 
*/

int TC, a, b, ans, num;

int main(void)
{
	scanf("%d", &TC);
	for (int tc = 0; tc < TC; tc++)
	{
		ans = 0; // 초기화 
		scanf("%d %d", &a, &b);
// num = b-a+1;
		num = b-a;
		// 가장 끝자리부터 오면서 %값만 구하기
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
