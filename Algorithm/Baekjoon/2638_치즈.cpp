/*
2638 ġ��
(2636 ġ��� ���� ����)
 
�߸� �����ߴ� ����
������ 0 �� 2�� �̻� �����ϸ� �������ٰ� �����ߴµ�
�ܺ� 0 �̶��� �����ؾ��� 

switching queue ����� ������� Ǯ��
0�� �� �ĺ� ġ� �־����, ���� �Ͽ� ġ� 0���� �ٲٸ� ���� ��������� ���� 

���� ����
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
�� 4 

https://www.acmicpc.net/board/view/89610
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
�� 3 

https://www.acmicpc.net/board/view/32174
9 9
0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0
0 1 0 0 0 0 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 0 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0
output
3

���� �Խ��� �ݷ� �亯�غ���
https://www.acmicpc.net/board/view/95911
https://www.acmicpc.net/board/view/14533
*/

// �ڵ� ����ϰ� ����
 
#include <stdio.h>
#define AIR (0)
#define CHEESE (1)
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int ch[101][101];
int touched[101][101]; // visited
struct heap{     
	int x;
	int y;
	int dist;
}airQ[10010], chQ[10010];
int air_fr, air_re;
int ch_fr, ch_re;
int N, M;
int ans = 0;
int flag = 1;
	
int is_melted(int x, int y) 
{
	int count = 0;
	for (int d = 0; d < 4; d++) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (nx >= N || nx < 0 || ny >= M || ny < 0) continue;
		if (ch[nx][ny] == AIR && touched[nx][ny]) count++;
	}
	if (count >= 2) return 1;
	return 0;
}

int main(void)
{
	// input
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &ch[i][j]);
		}
	}
	
	// start from outside
	airQ[air_re++] = {0, 0, 0};

	while (flag) {
		flag = 0;
		// change cheese to air
		while (ch_fr < ch_re) {
			heap current = chQ[ch_fr++];
			if (ans < current.dist) ans = current.dist;

			ch[current.x][current.y] = 0;	
			airQ[air_re++] = {current.x, current.y, current.dist};
			flag++;
		}
		// air BFS to find cheese
		while (air_fr < air_re) {
			heap current = airQ[air_fr++];
	
			for (int d = 0; d < 4; d++) {
				int nx = current.x + dx[d];
				int ny = current.y + dy[d];
				if (nx >= N || nx < 0 || ny >= M || ny < 0) continue;
				if (touched[nx][ny]) continue;
				if (ch[nx][ny] == AIR) {
					touched[nx][ny] = 1;
					airQ[air_re++] = {nx, ny, current.dist};
				}
				else if (ch[nx][ny] == CHEESE && is_melted(nx, ny)) {
					touched[nx][ny] = 1;
					chQ[ch_re++] = {nx, ny, current.dist+1};
				}
			}
			flag++;
		}
	}
	
	printf("%d\n", ans);

	return 0;
}

// ���� �� �ݷ� �°� ��ģ Ǯ��
// switching queue 
#if 0 
#include <stdio.h>
int N, M;
int ch[101][101];
int visited[101][101];
struct heap{     
	int x;
	int y;
	int dist;
}airQ[10010], chQ[10010];
int airfr, airre;
int chfr, chre;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int ans = 0;

int main(void)
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &ch[i][j]);
		}
	}
	
	airQ[airre++] = {0, 0, 0};
	int flag = 1;
	while (flag) {
		flag = 0;
		while (chfr < chre) {
			heap current = chQ[chfr++];
			ch[current.x][current.y] = 0;
			if (ans < current.dist) ans = current.dist;
			
			airQ[airre++] = {current.x, current.y, current.dist};
			flag++;
		}
		while (airfr < airre) {
			heap current = airQ[airfr++];
	
			for (int d = 0; d < 4; d++) {
				int nx = current.x + dx[d];
				int ny = current.y + dy[d];
				if (nx >= N || nx < 0 || ny >= M || ny < 0) continue;
				if (visited[nx][ny]) continue;
				if (ch[nx][ny] == 0) {
					visited[nx][ny] = 1;
					airQ[airre++] = {nx, ny, current.dist};
				}
				else if (ch[nx][ny] == 1) {
					int count = 0;
					for (int d2 = 0; d2 < 4; d2++) {
						int nx2 = nx + dx[d2];
						int ny2 = ny + dy[d2];
						if (nx2 >= N || nx2 < 0 || ny2 >= M || ny2 < 0) continue;
						if (ch[nx2][ny2] == 0 && visited[nx2][ny2]) count++;
					}
					if (count >= 2) {
						visited[nx][ny] = 1;
						chQ[chre++] = {nx, ny, current.dist+1};
					}
				}
			}
			flag++;
		}
	}
	
	printf("%d\n", ans);

	return 0;
}
#endif

// 2�� �̻� �����ϸ� ������ �������ٰ� ������ Ǯ�� 
#if 0
#include <stdio.h>
int N, M;
int ch[101][101];
int visited[101][101];
struct heap{     
	int x;
	int y;
	int dist;
}que[10010];
int fr, re;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int ans = 0;

int main(void)
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &ch[i][j]);
		}
	}
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (ch[i][j] == 0) {
				for (int d = 0; d < 4; d++) {
					int nx = i + dx[d];
					int ny = j + dy[d];
					if (nx >= N || nx < 0 || ny >= M || ny < 0) continue;
					if (ch[nx][ny] == 1) {
						// 2�� �̻� �־�� ť�� �߰� 
						int count = 0;
						for (int d2 = 0; d2 < 4; d2++) {
							int nx2 = nx + dx[d2];
							int ny2 = ny + dy[d2];
							if (nx2 >= N || nx2 < 0 || ny >= M || ny < 0) continue;
							if (ch[nx2][ny2] == 0) count++;
						}
						if (count >= 2) {
							visited[nx][ny] = 1;
							que[re++] = {nx, ny, 1};
						}
					}
				} 
			}
		}
	}
	
	while (fr < re) {
		heap current = que[fr++];
		ch[current.x][current.y] = 0;
		if (ans < current.dist) ans = current.dist;

		printf("%d\n", current.dist);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				printf("%d ", ch[i][j]);
			}
			printf("\n");
		} 

		for (int d = 0; d < 4; d++) {
			int nx = current.x + dx[d];
			int ny = current.y + dy[d];
			if (nx >= N || nx < 0 || ny >= M || ny < 0) continue;
			if (visited[nx][ny]) continue;
			if (ch[nx][ny] == 1) {
				int count = 0;
				for (int d2 = 0; d2 < 4; d2++) {
					int nx2 = nx + dx[d2];
					int ny2 = ny + dy[d2];
					if (nx2 >= N || nx2 < 0 || ny2 >= M || ny2 < 0) continue;
					if (ch[nx2][ny2] == 0) count++;
				}
				if (count >= 2) {
					visited[nx][ny] = 1;
					que[re++] = {nx, ny, current.dist+1};
				}
			}
		}
	}
	printf("%d\n", ans);

	return 0;
}
#endif
