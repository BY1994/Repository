/*
4485 ��� �� ���� �ְ� ������?

���ͽ�Ʈ��
BFS �δ� Ǯ �� ���� ����: �ִ� �Ÿ��� �����ع����� ���Ƽ� �����ϴ� ��찡 ��� �� ��
https://www.acmicpc.net/board/view/54214

Ǯ�� ���� �� �Ǽ��ߴ� ����
1. PQ �ȿ� cost ���� ������ �����ϴµ�, ó�� ���� �� ������ �� ����
(����غ��� dist ���� �ȿ� ������ �־ �߰�) 
2. dx, dy ���� ��Ÿ�� �־���
(����غ��� dist ���Ͱ� �Ʒ��θ� ������Ʈ�� �ǰ� ���������δ� ������Ʈ �� �� �� �߰�) 
*/

#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
const int INF = 1000000000;

int T, N;
vector<int> dist;
int miro[126][126];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void dijkstra(void){
	dist.clear();
	dist.resize(N*N+1, INF);
	
	dist[0] = 0;
	
	priority_queue<pair<int, int> > PQ;
	PQ.push(make_pair(-miro[0][0], 0));
	
	while (!PQ.empty()) {
		int cost = -PQ.top().first;
		int cur = PQ.top().second;
		PQ.pop();
		
		int x = cur / N;
		int y = cur % N;
		
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
			int ncost = cost + miro[nx][ny];
			int next = nx*N + ny;
			
			if (dist[next] > ncost) {
				dist[next] = ncost;
				PQ.push(make_pair(-ncost, next));
			}
		}
	}
}

int main(void) {
	
	while (1) {
		T++;
		scanf("%d", &N);
		if (N == 0) break;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &miro[i][j]);		
			}
		}

		dijkstra();
		
		printf("Problem %d: %d\n", T, dist[(N-1)*N + N-1]);
	}
	
    return 0;
}
