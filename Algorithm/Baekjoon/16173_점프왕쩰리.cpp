/*
16173 점프왕 쩰리 

dfs
*/

#include <stdio.h>

int game[4][4];
int visited[4][4];
int N;
int flag;
int dx[2] = {1, 0}; // 아래, 오른쪽 
int dy[2] = {0, 1};

void dfs(int x, int y) {
	if (flag) return;
	for (int d = 0; d < 2; ++d) {
		int nx = x + dx[d]*game[x][y];
		int ny = y + dy[d]*game[x][y];
		if (nx < 0 || nx > N || ny < 0 || ny > N) continue;
		if (visited[nx][ny]) continue;
		if (game[nx][ny] == -1) {
			flag = 1;
			return;
		}
		visited[nx][ny] = 1;
		dfs(nx, ny);
		visited[nx][ny] = 0;
	}
}

int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			scanf("%d", &game[i][j]);
		}
	}
	visited[0][0] = 1;
	dfs(0, 0);
	if (flag) printf("HaruHaru\n");
	else printf("Hing\n");

	return 0;
}
