/*
2712 �̱� ��Ÿ��

�Ҽ��� & �ݿø� 
*/

#include <stdio.h>
#include <math.h>

int main(void)
{
	int T;
	float value;
	char unit[3];

	scanf("%d", &T);
	while (T--) {
		scanf("%f ", &value);
		scanf("%s", unit);
		// ��°¥�� �ݿø�  
		if (unit[0] == 'k' && unit[1] == 'g') {
			printf("%.4f lb\n", round(value*22046)/10000);
		}
		else if (unit[0] == 'l' && unit[1] == 'b') {
			printf("%.4f kg\n", round(value*4536)/10000);
		}
		else if (unit[0] == 'l') {
			printf("%.4f g\n", round(value*2642)/10000);
		}
		else {
			printf("%.4f l\n", round(value*37854)/10000);
		}
	}	
	return 0;
}
