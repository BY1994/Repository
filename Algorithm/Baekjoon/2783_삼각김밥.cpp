/*
2783 삼각 김밥 

구현, 수학

지문에서 X, Y 가 반대로 읽혀서 이해하는데 한참 걸렸다.
들어오는 순서는 X, Y 인데, Y 그램당 X 원으로 설명해서.. 
*/

#include <stdio.h>

int main(void)
{
	int N;
	double X, Y;
	double ans, temp;
	
	scanf("%lf %lf", &X, &Y);
	ans = (X*1000)/Y;
	scanf("%d", &N);
	while (N--) {
		scanf("%lf %lf", &X, &Y);
		temp = (X*1000) / Y;
		if (ans > temp) ans = temp;
	}
	printf("%lf\n", ans);
	return 0;
}
