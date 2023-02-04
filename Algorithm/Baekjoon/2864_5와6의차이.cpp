/*
2864 5와 6의 차이 

그리디 / 사칙연산 
*/

#include <stdio.h>

int main(void)
{
	int A, B;
	int min = 0, max = 0;
	int mul = 1;
	scanf("%d %d", &A, &B);
	while (A || B) {

		if ((A % 10 == 5) || (A % 10 == 6)) {
			min += 5 * mul;
			max += 6 * mul;
		} else {
			min += (A % 10) * mul;
			max += (A % 10) * mul;
		}
		
		if ((B % 10 == 5) || (B % 10 == 6)) {
			min += 5 * mul;
			max += 6 * mul;
		} else {
			min += (B % 10) * mul;
			max += (B % 10) * mul;
		}
		A /= 10;
		B /= 10;
		
		mul *= 10;
	}
	printf("%d %d\n", min, max);
	return 0;
}
