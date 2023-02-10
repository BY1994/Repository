/*
2587 대표값2 

구현 / 정렬 
*/

#include <stdio.h>

int count[12];

int main(void) {
	int _sum = 0;
	int _count = 0;
	int num;
	for (int i = 0; i < 5; ++i) {
		scanf("%d", &num);
		_sum += num;
		count[num/10] += 1;
	}
	printf("%d\n", _sum / 5);

	for (int i = 1; i <= 10; ++i) {
		_count += count[i];
		if (_count >= 3) {
			printf("%d\n", i*10);
			break;
		}
	}
	
	return 0;
}
