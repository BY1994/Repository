/*
26169 �� �� �̳��� ����� ����

dfs 

�������� ��ֹ� ���ٴ� ���� ���� 
���� ó�� �ʿ���� 

Ʋ�ȴ� ����
1. apple, depth if �� ���� �ݴ�� �ؼ�
flag ó�� ��ȸ�� ���ȴ� ��
2. nx, ny ���� �� ��ǥ�� 5x5 ���� ũ�� ��������� Ȯ�� �� �� 
���� ���� �� ��Ÿ�� ������ �� ���� �� á����

�ݷ� ����� 
https://www.acmicpc.net/board/view/108824
3ĭ �Ʒ��� 2�� ��� ���� �� �ְ� ��ֹ��� �����ִ� ���
0 1 1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1 
0 0
�� 1
���� �ڵ� ��� 0 

�ݷ� �����2
0 0 1 1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
0 0
�� 1  
���� �ڵ� ���� ���� (move_count <= 3) 0 
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
