/*
2583 ���� ���ϱ�
 
���� Ǯ�鼭 ������� �κ�
1. ���� ����� �����ϴ� �κ�
������ ���� ��� x, y �� �ش��ϴ��� ���� �� ���ڿ� ���缭 �ڵ带 ®��. 
0, 0
        5, 7
2. c ��� sort ���̺귯�� ���� (�Ʒ� ��ũ ������) 
https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm
3. bfs �� cost �� +1 ���Ѽ� �ִ밪�� ���ߴµ�,
�̰� �ƴ϶� ��� ������ �� �ջ��ؾ��ϹǷ� ������ ������ �־��ߴ�.
bfs �� cost ������ ����. 

���� �亯�� ��û ������ ���� ���δ�.
���߿� ���� �亯 �ݷʸ� ã�� ������ ���� ������ �� ����. 
*/

#include <stdio.h>
#include <stdlib.h>

int M, N, K, x1, x2, y1, y2;

struct _q {
	int x;
	int y;
}q[20000];
int qs, qe;
int count;
int ans[101];
int paper[101][101];
int visited[101][101];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

int cmpfunc(const void *a, const void *b) {
	return (*(int*)a - *(int*)b);
}

int main(void)
{
	scanf("%d %d %d", &N, &M, &K);
	for (int i = 0; i < K; i++) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for (int a = y1; a < y2; a++) {
			for (int b = x1; b < x2; b++) {
				paper[a][b] = 1;
			}
		}
	}
	// 2 �� ���� ���鼭 ť ���� 
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (paper[i][j]) continue;
			if (visited[i][j]) continue;
			qs = qe = 0;
			int temp = 1;
			visited[i][j] = 1;
			q[qe++] = {i, j};
			while (qs < qe) {
				struct _q cur = q[qs++];

				for (int d = 0; d < 4; d++) {
					int nx = cur.x + dx[d];
					int ny = cur.y + dy[d];
					if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
					if (paper[nx][ny]) continue;
					if (visited[nx][ny]) continue;
					visited[nx][ny] = 1;
					temp++;
					q[qe++] = {nx, ny};
				}
			}
			ans[count++] = temp;				
		}
	} 		
	// sort �� ������ ans ���
	qsort(ans, count, sizeof(int), cmpfunc);
	printf("%d\n", count);
	for (int i = 0; i < count; i++) printf("%d ", ans[i]);
	printf("\n");
	return 0;
} 

#if 0  // ����� ���� 
#include <stdio.h>
#include <stdlib.h>

int M, N, K, x1, x2, y1, y2;

struct _q {
	int x;
	int y;
	int size;
}q[20000];
int qs, qe;
int count;
int ans[101];
int paper[101][101];
int visited[101][101];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

int cmpfunc(const void *a, const void *b) {
	return (*(int*)a - *(int*)b);
}

int main(void)
{
	scanf("%d %d %d", &N, &M, &K);
	for (int i = 0; i < K; i++) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for (int a = y1; a < y2; a++) {
			for (int b = x1; b < x2; b++) {
				paper[a][b] = 1;
			}
		}
	}
	#if 0 // ������ 
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d ", paper[i][j]);
		}
		printf("\n");
	}
	#endif
	// 2 �� ���� ���鼭 ť ���� 
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (paper[i][j]) continue;
			if (visited[i][j]) continue;
			qs = qe = 0;
			int temp = 1;
			visited[i][j] = 1;
			q[qe++] = {i, j, 1};
			while (qs < qe) {
				struct _q cur = q[qs++];
				//if (temp < cur.size) temp = cur.size;

				for (int d = 0; d < 4; d++) {
					int nx = cur.x + dx[d];
					int ny = cur.y + dy[d];
					if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
					if (paper[nx][ny]) continue;
					if (visited[nx][ny]) continue;
					visited[nx][ny] = 1;
					temp++;
					q[qe++] = {nx, ny, cur.size+1};
				}
			}
			ans[count++] = temp;				
		}
	} 		
	// sort �� ������ ans ���
	qsort(ans, count, sizeof(int), cmpfunc);
	printf("%d\n", count);
	for (int i = 0; i < count; i++) printf("%d ", ans[i]);
	printf("\n");
	return 0;
} 
#endif
