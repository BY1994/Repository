/*
11034 캥거루 세마리2

그리디 
가장 바깥쪽부터 채워야 최대가 될 테니까 
단순 거리 계산으로 가능 
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
