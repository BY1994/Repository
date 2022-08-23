/*
16928 ��� ��ٸ� ���� 

INF �� 101 �� �ϸ� ���� �� ���� (����?) 
���� ���� 
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
�� 3 

BFS �� �� Ǫ�� ������� �����ߴµ�...
visited �� ������ ����� �� �ƴϾ���. 
*/

// BFS
#include <stdio.h>
int ladder[101];
int snake[101];
int visited[101];
int ans;
struct q{
	int location;
	int cost;
}que[10000];
int qs, qe;


int main(void)
{
	int N, M, x, y;

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%d %d", &x, &y);
		ladder[x] = y;
	}
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &x, &y);
		snake[x] = y;
	}
	
	visited[1] = 1;
	que[qe++] = {1, 0};
	while (qs < qe) {
		struct q current = que[qs++];
		if (current.location == 100) {
			ans = current.cost;
			break;
		}

		for (int dice = 1; dice <= 6; dice++) {
			int next = current.location + dice;
			if (next > 100) break;
			if (ladder[next]) next = ladder[next];
			else if (snake[next]) next = snake[next];
			if (visited[next]) continue;
			visited[next] = 1;
			que[qe++] = {next, current.cost+1};
		}
	}
	printf("%d\n", ans);
	return 0;
}

// dfs �ð� �ʰ� ����� 
#if 0
#include <stdio.h>
#define INF (200)
int ladder[101];
int snake[101];
int visited[101];
int ans = INF;

void dfs(int current, int count)
{
	if (count > ans) return;
	if (current == 100) {
		if (ans > count) ans = count;
		return;
	}

	for (int dice = 1; dice <= 6; dice++) {
		int next = current + dice;
		if (next > 100) break;
		if (ladder[next]) next = ladder[next];
		else if (snake[next]) next = snake[next];
		if (visited[next]) continue;
		visited[next] = 1;
		dfs(next, count + 1);
		visited[next] = 0;
	}
}

int main(void)
{
	int N, M, x, y;

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%d %d", &x, &y);
		ladder[x] = y;
	}
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &x, &y);
		snake[x] = y;
	}
	visited[1] = 1;
	dfs(1, 0);
	printf("%d\n", ans);
	return 0;
}
#endif
