/*
5787 Noise Effect

Brute Force
토큰이 옆으로만 돌아가고 뒤집히는 경우는 없다고 생각했는데
문제 예제를 보니 첫번째 예제가 뒤집히는 경우였다.
풀 때 실수가 잠깐 있었던 건 배열을 stack 영역에 만들면서 초기화를 안 했던 것,
while 문 안에서 초기화하지 않아서 누적이 생겼던 것이 있었다. 
*/

#include <stdio.h>
#include <stdlib.h>

int token[401][401];
int scanned[401][401];

int main(void)
{
	int N, ni, nj;
	while (1) {
		int max = 0;
		int candidates[8] = {0,};
		scanf("%d", &N);
		if (N == 0) return 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &token[i][j]);
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &scanned[i][j]);
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (abs(token[i][j] - scanned[i][j]) <= 100) candidates[0]++;
				if (abs(token[i][N-1-j] - scanned[i][j]) <= 100) candidates[1]++;
				
				if (abs(token[N-1-j][i] - scanned[i][j]) <= 100) candidates[2]++;
				if (abs(token[N-1-j][N-1-i] - scanned[i][j]) <= 100) candidates[3]++;

				if (abs(token[N-1-i][N-1-j] - scanned[i][j]) <= 100) candidates[4]++;
				if (abs(token[N-1-i][j] - scanned[i][j]) <= 100) candidates[5]++;

				if (abs(token[j][N-1-i] - scanned[i][j]) <= 100) candidates[6]++;				
				if (abs(token[j][i] - scanned[i][j]) <= 100) candidates[7]++;
			}
		}

		for (int i = 0; i < 8; i++) if (candidates[i] > max) max = candidates[i];	

		printf("%.2f\n", (float)max*100/(float)(N*N));
	}
	return 0;
}

// 토큰을 뒤집는 경우가 없다고 생각하고 돌리기만 했더니 예제 안 나옴
#if 0 
#include <stdio.h>
#include <stdlib.h>

int token[401][401];
int scanned[401][401];

int main(void)
{
	int N;
	while (1) {
		int max = 0;
		int temp;
		scanf("%d", &N);
		if (N == 0) return 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &token[i][j]);
			}
		}
		// 1. original
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &scanned[i][j]);
				if (abs(token[i][j] - scanned[i][j]) <= 100) max++;
			}
		}
		// 2. 90 degree
		temp = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int ni = N-1-j;
				int nj = i;
				if (abs(token[ni][nj] - scanned[i][j]) <= 100) temp++;
			}
		}
		if (max < temp) max = temp;
		// 3. 180 degree
		temp = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int ni = N-1-i;
				int nj = N-1-j;
				if (abs(token[ni][nj] - scanned[i][j]) <= 100) temp++;
			}
		}
		if (max < temp) max = temp;
		// 4. 270 degree
		temp = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int ni = j;
				int nj = N-1-i;
				if (abs(token[ni][nj] - scanned[i][j]) <= 100) temp++;
			}
		}
		if (max < temp) max = temp;
		
		printf("%d\n", max);
		printf("%.2f\n", (float)max*100/(float)(N*N));
	}
	return 0;
}
#endif
