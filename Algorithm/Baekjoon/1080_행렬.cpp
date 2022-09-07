/*
1080 행렬

greedy

그리디 문제라서 이렇게 될 것 같아서 풀긴 했는데
엄밀한 증명은 어렵다.
왜 그리디인가에 대해 다른 사람이 작성한 게시글은 아래와 같다.
https://www.acmicpc.net/board/view/76546 
"최적해에는 중복으로 flip하는 것이 없다는 사실을 알고 있다면,"
*/

#include <stdio.h>

int N, M;
int ans;

int before[51][51];
int after[51][51];

void input(void) {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &before[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &after[i][j]);
		}
	}	
}

void flip_subarray(int x, int y) {
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			before[x+i][y+j] = (before[x+i][y+j] + 1) % 2;
		}
	}
}

void flip(void){
	for (int i = 0; i <= N-3; i++) {
		for (int j = 0; j <= M-3; j++) {
			if (before[i][j] != after[i][j]) {
				flip_subarray(i, j);
				ans++;
			}
		}
	}
}

int evaluate(void) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (before[i][j] != after[i][j])
				return -1;
		}
	}
	return ans;
}

int main(void)
{
	input();

	flip();
	
	printf("%d\n", evaluate());

	return 0;
}
