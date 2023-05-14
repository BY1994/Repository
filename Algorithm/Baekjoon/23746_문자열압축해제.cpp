/*
23746 문자열 압축 해제 
*/

#include <stdio.h>
char SPC[256][1001];
char temp[1001];
char comp[1001];
char decomp[1000001];

int main(void)
{
	int N, S, E;
	int d = 0;
	char C;
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%s", temp);
		getchar();
		scanf("%c", &C);
		getchar();
		for (int j = 0; temp[j]; ++j) SPC[C][j] = temp[j];
	}
	scanf("%s", comp);
	scanf("%d %d", &S, &E);

	for (int i = 0; comp[i]; ++i) {
		for (int j = 0; SPC[comp[i]][j]; ++j) {
			decomp[d++] = SPC[comp[i]][j];
		}
	}
	for (int i = S-1; i < E; ++i) printf("%c", decomp[i]);
	return 0;
}
