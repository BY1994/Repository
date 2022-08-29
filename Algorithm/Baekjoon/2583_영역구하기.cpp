/*
2583 영역 구하기
 
문제 풀면서 힘들었던 부분
1. 맵을 뒤집어서 생각하는 부분
예제를 보고 어떤게 x, y 에 해당하는지 보고 그 숫자에 맞춰서 코드를 짰다. 
0, 0
        5, 7
2. c 언어 sort 라이브러리 사용법 (아래 링크 참고함) 
https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm
3. bfs 에 cost 를 +1 시켜서 최대값을 구했는데,
이게 아니라 모든 영역을 다 합산해야하므로 별도의 변수를 둬야했다.
bfs 의 cost 로직은 뺐다. 

질문 답변에 엄청 질문이 많이 보인다.
나중에 질문 답변 반례를 찾고 싶으면 좋은 문제인 것 같다. 
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
	// 2 중 포문 돌면서 큐 시작 
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
	// sort 한 다음에 ans 출력
	qsort(ans, count, sizeof(int), cmpfunc);
	printf("%d\n", count);
	for (int i = 0; i < count; i++) printf("%d ", ans[i]);
	printf("\n");
	return 0;
} 

#if 0  // 디버깅 버전 
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
	#if 0 // 디버깅용 
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d ", paper[i][j]);
		}
		printf("\n");
	}
	#endif
	// 2 중 포문 돌면서 큐 시작 
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
	// sort 한 다음에 ans 출력
	qsort(ans, count, sizeof(int), cmpfunc);
	printf("%d\n", count);
	for (int i = 0; i < count; i++) printf("%d ", ans[i]);
	printf("\n");
	return 0;
} 
#endif
