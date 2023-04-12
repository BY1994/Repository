/*
5719 거의 최단경로 

다익스트라 
https://yabmoons.tistory.com/364
여러 최단 경로 저장 방법 
https://www.acmicpc.net/board/view/35229

초기화를 제대로 안 해줘서 하나씩 출력하면 답이 나오는데,
여러 테스트케이스를 출력하면 답이 안 나왔다.
vector 사용시 초기화 반드시 적어주기
+ priority queue 초기화가 빠져있었는데, clear 메소드가 없어서 매번 선언해줘야한다. 
질문 게시판의 단편적인 반례들로는 찾을 수 없는 버그였다.
엄청 여러 테스트케이스를 넣어봐야 찾았을 것 
+ 질문 게시판의 반례들로는 찾을 수 없었던 문제가 있었다.
find_shortest 함수에서 if 로 체크를 하지 않으면
무한 루프를 도는 경우가 생기는 것으로 보인다. 
아래 인풋 생성기로 만들어진 대형 인풋에서 문제가 되는 걸 발견하였다. 

질문 게시판을 보면 최단 경로 탐색시 bfs 를 쓴 사람이 많은데,
굳이 완전탐색 하지 않아도 다익스트라로 가능하다. 

인풋 생성기
https://www.acmicpc.net/board/view/50647 

23-04-09 틀렸습니다
1. find_shortest 에 왜 if 가 필요한 건지 정확히 이해 못 함 
=> 무한루프는 안 생기더라도, 입력이 엄청 커지면 재귀를 너무 많이 도는 경우가 생길 수 있을 것으로 보인다.
똑같은 지점을 몇번이고 반복해서 들어가서 문제가 될 수 있을 것이다. 
2. 틀린점은 dist[0] 이 아닌 dist[S] 를 0 으로 설정해야했다. 

23-04-12 맞았습니다 
*/

// 맞은 풀이
#include <iostream>
#include <vector>
#include <queue>
#define INF 99999999
using namespace std;

int dist[501];
int block[501][501];
vector<int> path[501];
int edge[501][501]; 

void find_shortest(int cur, int S) {
	if (cur == S) return;
	for (int i = 0; i < path[cur].size(); ++i) {
		if (block[path[cur][i]][cur] == 1) continue;
		block[path[cur][i]][cur] = 1;
		find_shortest(path[cur][i], S);
	}
}

int main(void) {
	int N, M, S, D;
	int U, V, P;

	ios::sync_with_stdio(0);
	cin.tie(0);
	while (1) {
		cin >> N >> M;
		if ((N == 0) && (M == 0)) break;
		cin >> S >> D; // 시작점, 도착점 (0~N-1) 
		
		// 초기화 
		priority_queue<pair<int, int> > PQ1;
		priority_queue<pair<int, int> > PQ2;

		for (int i = 0; i < N; ++i) {
			dist[i] = INF;
			path[i].clear();
			for (int j = 0; j < N; ++j)
				edge[i][j] = block[i][j] = 0;
		}
		for (int i = 0; i < M; ++i) {
			cin >> U >> V >> P;
			edge[U][V] = P;
		}

		// 최단 경로 탐색 
		dist[S] = 0;
		PQ1.push(make_pair(0, S));
		while (PQ1.empty() == 0) {
			int cost = -PQ1.top().first;
			int cur = PQ1.top().second;
			PQ1.pop();
			
			for (int i = 0; i < N; ++i) {
				if (edge[cur][i] == 0) continue;
				int next = i;
				int ncost = edge[cur][i];
				
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ1.push(make_pair(-dist[next], next));
					path[next].clear();
					path[next].push_back(cur);
				} else if (dist[next] == cost + ncost) {
					path[next].push_back(cur);
				}
			}
		}
		if (dist[D] == INF) {
			cout << -1 << '\n';
			continue;
		}
		
		// 최단경로의 path 를 돌면서 block 체크
		find_shortest(D, S);

		// block 을 피해서 차선의 최단 경로 탐색 
		for (int i = 0; i < N; ++i) dist[i] = INF;
		dist[S] = 0;
		PQ2.push(make_pair(0, S));
		while (PQ2.empty() == 0) {
			int cost = -PQ2.top().first;
			int cur = PQ2.top().second;
			PQ2.pop();
			
			for (int i = 0; i < N; ++i) {
				if (edge[cur][i] == 0) continue;
				int next = i;
				int ncost = edge[cur][i];
				if (block[cur][next]) continue;
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ2.push(make_pair(-dist[next], next));
				}
			}
		}
		if (dist[D] == INF) cout << -1 << '\n';
		else cout << dist[D] << '\n';
	}
	return 0;
}

// 틀린 풀이 (dist[0] 초기화 실수) 
#if 0
#include <iostream>
#include <vector>
#include <queue>
#define INF 99999999
using namespace std;

int dist[501];
int block[501][501];
vector<int> path[501];
int edge[501][501]; 

void find_shortest(int cur, int S) {
	if (cur == S) return;
	for (int i = 0; i < path[cur].size(); ++i) {
		if (block[path[cur][i]][cur] == 1) continue;
		block[path[cur][i]][cur] = 1;
		find_shortest(path[cur][i], S);
	}
}

int main(void) {
	int N, M, S, D;
	int U, V, P;

	//ios::sync_with_stdio(0);
	//cin.tie(0);
	while (1) {
		cin >> N >> M;
		if ((N == 0) && (M == 0)) break;
		cin >> S >> D; // 시작점, 도착점 (0~N-1) 
		
		// 초기화 
		priority_queue<pair<int, int> > PQ1;
		priority_queue<pair<int, int> > PQ2;

		for (int i = 0; i < N; ++i) {
			dist[i] = INF;
			path[i].clear();
			for (int j = 0; j < N; ++j)
				edge[i][j] = block[i][j] = 0;
		}
		for (int i = 0; i < M; ++i) {
			cin >> U >> V >> P;
			edge[U][V] = P;
		}

		// 최단 경로 탐색 
		dist[0] = 0;
		PQ1.push(make_pair(0, S));
		while (PQ1.empty() == 0) {
			int cost = -PQ1.top().first;
			int cur = PQ1.top().second;
			PQ1.pop();
			
			for (int i = 0; i < N; ++i) {
				if (edge[cur][i] == 0) continue;
				int next = i;
				int ncost = edge[cur][i];
				
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ1.push(make_pair(-dist[next], next));
					path[next].clear();
					path[next].push_back(cur);
				} else if (dist[next] == cost + ncost) {
					path[next].push_back(cur);
				}
			}
		}
		if (dist[D] == INF) {
			cout << -1 << '\n';
			continue;
		}
		
		// 최단경로의 path 를 돌면서 block 체크
		find_shortest(D, S);

		// block 을 피해서 차선의 최단 경로 탐색 
		for (int i = 1; i < N; ++i) dist[i] = INF;
		PQ2.push(make_pair(0, S));
		while (PQ2.empty() == 0) {
			int cost = -PQ2.top().first;
			int cur = PQ2.top().second;
			PQ2.pop();
			
			for (int i = 0; i < N; ++i) {
				if (edge[cur][i] == 0) continue;
				int next = i;
				int ncost = edge[cur][i];
				if (block[cur][next]) continue;
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ2.push(make_pair(-dist[next], next));
				}
			}
		}
		if (dist[D] == INF) cout << -1 << '\n';
		else cout << dist[D] << '\n';
	}
	return 0;
}
#endif

// 틀린 풀이
#if 0
#include <iostream>
#include <vector>
#include <queue>
#define INF (99999999)
using namespace std;

int dist[501];
int block[501][501];
vector<int> path[501];
vector<pair<int, int> > edge[501];

void find_shortest(int cur, int S) {
	if (cur == S) return;
	for (int i = 0; i < path[cur].size(); ++i) {
		block[path[cur][i]][cur] = 1;
		find_shortest(path[cur][i], S);
	}
}

int main(void) {
	int N, M, S, D;
	int U, V, P;

	while (1) {
		cin >> N >> M;
		if ((N == 0) && (M == 0)) break;
		cin >> S >> D; // 시작점, 도착점 (0~N-1) 
		
		// 초기화 
		priority_queue<pair<int, int> > PQ1;
		priority_queue<pair<int, int> > PQ2;

		for (int i = 0; i < N; ++i) {
			dist[i] = INF;
			path[i].clear();
			edge[i].clear();
			for (int j = 0; j < N; ++j)
				block[i][j] = 0;
		}
		for (int i = 0; i < M; ++i) {
			cin >> U >> V >> P;
			edge[U].push_back(make_pair(V, P));
		}

		// 최단 경로 탐색 
		dist[0] = 0;
		PQ1.push(make_pair(0, S));
		while (PQ1.empty() == 0) {
			int cost = -PQ1.top().first;
			int cur = PQ1.top().second;
			PQ1.pop();
			
			for (int i = 0; i < edge[cur].size(); ++i) {
				int next = edge[cur][i].first;
				int ncost = edge[cur][i].second;
				
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ1.push(make_pair(-dist[next], next));
					path[next].clear();
					path[next].push_back(cur);
				} else if (dist[next] == cost + ncost) {
					path[next].push_back(cur);
				}
			}
		}
		if (dist[D] == INF) {
			cout << -1 << '\n';
			continue;
		}
		
		// 최단경로의 path 를 돌면서 block 체크
		find_shortest(D, S);

		// block 을 피해서 차선의 최단 경로 탐색 
		for (int i = 1; i < N; ++i) dist[i] = INF;
		PQ2.push(make_pair(0, S));
		while (PQ2.empty() == 0) {
			int cost = -PQ2.top().first;
			int cur = PQ2.top().second;
			PQ2.pop();
			
			for (int i = 0; i < edge[cur].size(); ++i) {
				int next = edge[cur][i].first;
				int ncost = edge[cur][i].second;
				if (block[cur][next]) continue;
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ2.push(make_pair(-dist[next], next));
				}
			}
		}
		if (dist[D] == INF) cout << -1 << '\n';
		else cout << dist[D] << '\n';
	}
	return 0;
}
#endif 

// 잘못 짠 풀이
// 다익스트라를 돌려서 최단 경로를 1개만 찾는 것이 아님
// 여러 경로를 다 확인할 수 있어야함 
#if 0 
#include <iostream>
#include <vector>
#include <queue>
#define INF (999999)
using namespace std;

int dist[501];
int path[501];
int block[501];
vector<pair<int, int> > edge[501];
priority_queue<pair<int, int> > PQ1;
priority_queue<pair<int, int> > PQ2;

int main(void) {
	int N, M, S, D;
	int U, V, P;
	// 인접리스트
	ios::sync_with_stdio(0);
	cin.tie(0);
	while (1) {
		cin >> N >> M;
		if (N == 0 && M == 0) break;
		cin >> S >> D; // 시작점, 도착점 (0~N-1) 
		for (int i = 0; i < M; ++i) {
			cin >> U >> V >> P;
			edge[U].push_back(make_pair(V, P));
		}
		// 시작점은 0 
		for (int i = 1; i < N; ++i) dist[i] = INF;
		for (int i = 0; i < N; ++i) block[i] = 0;
		for (int i = 0; i < N; ++i) path[i] = -1;
		PQ1.push(make_pair(0, S));
		while (PQ1.empty() == 0) {
			int cost = -PQ1.top().first;
			int cur = PQ1.top().second;
			PQ1.pop();
			
			for (int i = 0; i < edge[cur].size(); ++i) {
				int next = edge[cur][i].first;
				int ncost = edge[cur][i].second;
				
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ1.push(make_pair(-dist[next], next));
					path[next] = cur;
				}
			}
		}
		// path 를 돌면서 block 체크
		int node = path[D];
		while (node != S && node != -1) {
			block[node] = 1;
			node = path[node];
		}
		if (node == -1) {
			cout << -1 << '\n';
			continue;
		}
		// block 을 피해서 다익스트라
		for (int i = 1; i < N; ++i) dist[i] = INF;
		PQ2.push(make_pair(0, S));
		while (PQ2.empty() == 0) {
			int cost = -PQ2.top().first;
			int cur = PQ2.top().second;
			PQ2.pop();
			
			for (int i = 0; i < edge[cur].size(); ++i) {
				int next = edge[cur][i].first;
				int ncost = edge[cur][i].second;
				if (block[next]) continue;				
				if (dist[next] > cost + ncost) {
					dist[next] = cost + ncost;
					PQ2.push(make_pair(-dist[next], next));
				}
			}
		}
		if (dist[D] == INF) cout << -1 << '\n';
		else cout << dist[D] << '\n';
	}
	return 0;
}
#endif
