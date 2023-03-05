/*
26169 세 번 이내에 사과를 먹자

dfs 

시작점에 장애물 없다는 조건 있음 
예외 처리 필요없음 

틀렸던 이유
1. apple, depth if 문 순서 반대로 해서
flag 처리 기회를 날렸던 것
2. nx, ny 구할 때 좌표가 5x5 보드 크기 벗어나는지를 확인 안 함 
예제 돌릴 때 런타임 에러가 안 나서 못 찼았음

반례 만들기 
https://www.acmicpc.net/board/view/108824
3칸 아래로 2개 사과 먹을 수 있고 장애물로 막혀있는 경우
0 1 1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1 
0 0
답 1
위의 코드 출력 0 

반례 만들기2
0 0 1 1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
0 0
답 1  
위의 코드 수정 버전 (move_count <= 3) 0 
*/

#include <stdio.h>
int visited[5][5];
int board[5][5];
int flag;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void dfs(int curx, int cury, int depth, int apple) {
	if (flag) return;
	if (apple >= 2) {
		flag = 1;
		return;
	}
	if (depth >= 3) return;
	
	for (int d = 0; d < 4; ++d) {
		int nx = curx + dx[d];
		int ny = cury + dy[d];
		
		if (nx > 4 || nx < 0 || ny > 4 || ny < 0) continue;
		if (board[nx][ny] == -1) continue;
		if (visited[nx][ny]) continue;
		if (board[nx][ny] == 1) {
			visited[nx][ny] = 1;
			dfs(nx, ny, depth+1, apple+1);
			visited[nx][ny] = 0;
		} else {
			visited[nx][ny] = 1;
			dfs(nx, ny, depth+1, apple);
			visited[nx][ny] = 0;
		}
	}
}

int main(void) {
	int sx, sy;

	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 5; ++j) {
			scanf("%d", &board[i][j]);
		}
	}
	scanf("%d %d", &sx, &sy);
	visited[sx][sy] = 1;
	dfs(sx, sy, 0, 0);
	if (flag) printf("1\n");
	else printf("0\n");

	return 0;
}
