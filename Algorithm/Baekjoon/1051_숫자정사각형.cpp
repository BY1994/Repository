/*
1051 ���� ���簢�� 

brute force

���� ���� �ݷ� 
3 5
12345
67800
23400

�����亯 �ݷ� ����� 
https://www.acmicpc.net/board/view/102415
3 6
122145
322345
133145
=> ���� ����� �� ������� �����ߴµ�, �ڵ带 �߸� �����ߴ�. 
size �� ���� ũ�� �÷����鼭 ���� ������ �̷� ������ ������.
�Է� �κ��� ��������. (%1d ���� �ϴµ� %d ��� �Է¹���) 
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

// Ʋ�Ƚ��ϴ�
// ������ �� �¾Ҵµ� �����غ��� size �� ������ ���� �� �ȴ�...!!
// �� size ���� ���� ��찡 ���� ���� �ֱ� ������ 
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
