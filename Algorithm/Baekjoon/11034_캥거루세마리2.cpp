/*
11034 Ļ�ŷ� ������2

�׸��� 
���� �ٱ��ʺ��� ä���� �ִ밡 �� �״ϱ� 
�ܼ� �Ÿ� ������� ���� 
*/

#include <stdio.h>
#include <math.h>

int main(void) {
	int A, B, C, AB, BC;
	while (scanf("%d %d %d", &A, &B, &C) != -1) {
		AB = abs(A - B);
		BC = abs(B - C);
		if (AB > BC) printf("%d\n", AB-1);
		else printf("%d\n", BC-1);
	}
	return 0;
}
