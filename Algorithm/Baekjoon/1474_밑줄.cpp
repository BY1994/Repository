/*
1474 밑 줄 

greedy
최대 1개 밖에 차이가 나지 않으므로
소문자 앞에 넣는 것, 남은 개수가 딱 맞으면 무조건 넣는 것
으로 해도 된다. (greedy) 
*/

#include <stdio.h>
#include <string.h>
char words[10][11];

int main(void)
{
	int N, M, div, rem, total = 0;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		scanf("%s", words[i]);
		total += strlen(words[i]);
	}
	total = M - total;
	div = total / (N-1);
	rem = total - (div*(N-1));
	printf("%s", words[0]);
	for (int i = 1; i < N; ++i) {
		for (int j = 0; j < div; ++j) printf("_");
		if (rem >= (N-i) || (rem > 0 && words[i][0] >= 'a')) {
			printf("_");
			rem--;
		}
		printf("%s", words[i]);
	}
	printf("\n");
	return 0;
}
