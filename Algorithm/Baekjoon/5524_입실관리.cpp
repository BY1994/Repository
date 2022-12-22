/*
5524 입실 관리

문자열 
*/

#include <stdio.h>

int main(void)
{
	int N;
	char name[101];
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%s", name);
		for (int j = 0; name[j]; ++j) {
			if (name[j] <= 'Z') {
				name[j] += 'a' - 'A';
			} 
		}
		printf("%s\n", name);
	}
	return 0;
}
