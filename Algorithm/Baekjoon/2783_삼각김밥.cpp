/*
2783 �ﰢ ��� 

����, ����

�������� X, Y �� �ݴ�� ������ �����ϴµ� ���� �ɷȴ�.
������ ������ X, Y �ε�, Y �׷��� X ������ �����ؼ�.. 
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
