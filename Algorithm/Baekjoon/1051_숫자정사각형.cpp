/*
1051 숫자 정사각형 

brute force

내가 만든 반례 
3 5
12345
67800
23400

질문답변 반례 만들기 
https://www.acmicpc.net/board/view/102415
3 6
122145
322345
133145
=> 답을 덮어쓰는 게 문제라고 생각했는데, 코드를 잘못 이해했다. 
size 를 점점 크게 늘려가면서 보기 때문에 이런 문제는 없었다.
입력 부분이 문제였다. (%1d 여야 하는데 %d 라고 입력받음) 
*/
#include <stdio.h>

int Rect[51][51];

int max(int a, int b) {
	return (a > b)? a:b;
}

int min(int a, int b) {
	return (a > b)? b:a;
}

int main(void) {
	int N, M, size, _max = 1;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf("%1d", &Rect[i][j]);
		}
	}
	size = min(N, M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			for (int k = 1; k < size; ++k) {
				if (i + k >= N) break;
				if (j + k >= M) break;
				if ((Rect[i][j] == Rect[i+k][j]) && (Rect[i][j] == Rect[i][j+k]) \
					&& (Rect[i][j] == Rect[i+k][j+k])) {
					_max = max(_max, k+1);
				}
			}
		}
	}
	printf("%d\n", _max * _max);
	return 0;
} 

// 틀렸습니다
// 예제는 다 맞았는데 생각해보니 size 를 무조건 빼면 안 된다...!!
// 그 size 보다 작은 경우가 답일 수도 있기 때문에 
#if 0
#include <stdio.h>

int Rect[51][51];

int max(int a, int b) {
	return (a > b)? a:b;
}

int min(int a, int b) {
	return (a > b)? b:a;
}

int main(void) {
	int N, M, size, _max = 1;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf("%1d", &Rect[i][j]);
		}
	}
	size = min(N, M);
	for (int i = 0; i <= N - size; ++i) {
		for (int j = 0; j <= M - size; ++j) {
			for (int k = 1; k < size; ++k) {
				if ((Rect[i][j] == Rect[i+k][j]) && (Rect[i][j] == Rect[i][j+k]) \
					&& (Rect[i][j] == Rect[i+k][j+k])) {
					_max = max(_max, k+1);
				}
			}
		}
	}
	printf("%d\n", _max * _max);
	return 0;
} 
#endif
