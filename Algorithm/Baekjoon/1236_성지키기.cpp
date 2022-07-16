/*
1236 성 지키기 

50x50 은 백트래킹으로 못할 듯
2^250 이기 때문에 2초 시간 제한 안에 못 돈다. 

1
 2
  3
   4
이런 식으로 가야 최적이고,
비어있는 곳을 찾아서 이렇게 넣어주면 되는데
ex)
 X
1
  3
   4
만일 비어있는 곳이 없다면, 따로 처리해줘야함
1234
 X
  X
   X

내 풀이는,
행, 열이 다 비어있을 때 그 지점을 일단 채우고 보는 것
그래도 다 안 채워지는 경우가 있는데, 그러면 행이나 열 중 한 쪽만 빌 것이다.
그것만 + 시켜줌
    1
	 // 채우려고 보면 열이 다 차서 둘 곳이 없음 
	
2345 

다른 사람의 아이디어를 보니
단순히 행/열 중 더 큰 값을 출력해도 되는 것 같다. 
https://www.acmicpc.net/board/view/45206
*/

#include <stdio.h>

int N, M;
char castle[51][51];
int visited[51][51];
int guard_x[51];
int guard_y[51];
int ans;

int main(void)
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf(" %c", &castle[i][j]);
			if (castle[i][j] == 'X') {
				guard_y[j] += 1;
				guard_x[i] += 1;				
			}
		}
	}
	for (int i = 0; i < N; ++i) {
		if (guard_x[i]) continue;
		for (int j = 0; j < M; ++j) {
			if (guard_y[j]) continue;
			guard_y[j] = 1;
			guard_x[i] = 1;
			ans += 1;
			break;
		}
	}
	for (int i = 0; i < N; ++i) {
		if (guard_x[i]) continue;
		ans += 1;
	}
	for (int j = 0; j < M; ++j) {
		if (guard_y[j]) continue;
		ans += 1;
	}

	printf("%d\n", ans);
	return 0;
}

// 시간초과 예상 (백트래킹) 
#if 0
#include <stdio.h>

int N, M;
char castle[51][51];
int visited[51][51];
int guard_x[51];
int guard_y[51];
int ans = 1000;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void backtracking(int x, int y, int cur)
{
	if (cur > ans) return;
	
	// 모든 행과 모든 열에 경비원 있는지
	int flag = 0;
	for (int i = 0; i < N; ++i) {
		if (guard_x[i] == 0) {
			//printf("guard x%d\n", i);
			flag = 1;
			break;
		}
	}
	for (int i = 0; i < M; ++i) {
		if (guard_y[i] == 0) {
			//printf("guard y%d\n", i);
			flag = 1;
			break;
		}
	}
	if (flag == 0) {
		if (ans > cur) ans = cur;
		return;		
	}
	
	for (int d = 0; d < 4; d++) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
		if (visited[nx][ny] == 1) continue;
		if (castle[nx][ny] == 'X') continue;
		visited[nx][ny] = 1;
		guard_x[nx] += 1;
		guard_y[ny] += 1;
		backtracking(nx, ny, cur+1);
		guard_x[nx] -= 1;
		guard_y[ny] -= 1;
		visited[nx][ny] = 0;
		
		visited[nx][ny] = 1;
		backtracking(nx, ny, cur);
		visited[nx][ny] = 0;
	}
}

int main(void)
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf(" %c", &castle[i][j]);
			//printf("%d %d (%c)\n", i, j, castle[i][j]);
			if (castle[i][j] == 'X') {
				guard_y[j] += 1;
				guard_x[i] += 1;				
			}
		}
	}
	if (castle[0][0] == '.') {
		visited[0][0] = 1;
		guard_x[0] += 1;
		backtracking(0, 0, 1);
		guard_x[0] -= 1;
		visited[0][0] = 0;	
	}
	visited[0][0] = 1;
	backtracking(0, 0, 0);
	visited[0][0] = 0;
	
	printf("%d\n", ans);
	return 0;
}
#endif
