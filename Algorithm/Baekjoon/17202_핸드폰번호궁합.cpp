/*
17202 핸드폰 번호 궁합 

다이나믹 프로그래밍으로 분류되어있어서 푼 문제
단순 덧셈 문제였다. 

문제 예제 1 번 입력 한 줄로 잘못 받았는데... 그래도 답이 나왔다;; 
*/

#include <stdio.h>

int array[17];

int main(void) {
	for (int i = 0; i < 16; i += 2) scanf("%1d", &array[i]);
	for (int i = 1; i < 16; i += 2) scanf("%1d", &array[i]);
	for (int i = 16; i > 2; --i) {
		for (int j = 0; j < i-1; ++j) {
			array[j] = (array[j] + array[j+1]) % 10;
		}
	}
	printf("%d%d\n", array[0], array[1]);
	return 0;
}
