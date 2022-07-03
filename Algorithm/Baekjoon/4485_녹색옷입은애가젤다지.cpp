/*
4485 녹색 옷 입은 애가 젤다지?

다익스트라
BFS 로는 풀 수 없는 이유: 최단 거리로 도착해버리면 돌아서 도착하는 경우가 고려 안 됨
https://www.acmicpc.net/board/view/54214

풀이 과정 중 실수했던 내용
1. PQ 안에 cost 값을 음수로 관리하는데, 처음 넣을 때 음수로 안 넣음
(출력해보니 dist 벡터 안에 음수가 있어서 발견) 
2. dx, dy 값에 오타가 있었음
(출력해보니 dist 벡터가 아래로만 업데이트가 되고 오른쪽으로는 업데이트 안 된 걸 발견) 
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
