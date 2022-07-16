/*
1236 �� ��Ű�� 

50x50 �� ��Ʈ��ŷ���� ���� ��
2^250 �̱� ������ 2�� �ð� ���� �ȿ� �� ����. 

1
 2
  3
   4
�̷� ������ ���� �����̰�,
����ִ� ���� ã�Ƽ� �̷��� �־��ָ� �Ǵµ�
ex)
 X
1
  3
   4
���� ����ִ� ���� ���ٸ�, ���� ó���������
1234
 X
  X
   X

�� Ǯ�̴�,
��, ���� �� ������� �� �� ������ �ϴ� ä��� ���� ��
�׷��� �� �� ä������ ��찡 �ִµ�, �׷��� ���̳� �� �� �� �ʸ� �� ���̴�.
�װ͸� + ������
    1
	 // ä����� ���� ���� �� ���� �� ���� ���� 
	
2345 

�ٸ� ����� ���̵� ����
�ܼ��� ��/�� �� �� ū ���� ����ص� �Ǵ� �� ����. 
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

// �ð��ʰ� ���� (��Ʈ��ŷ) 
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
	
	// ��� ��� ��� ���� ���� �ִ���
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
