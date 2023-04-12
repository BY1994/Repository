/*
5719 ���� �ִܰ�� 

���ͽ�Ʈ�� 
https://yabmoons.tistory.com/364
���� �ִ� ��� ���� ��� 
https://www.acmicpc.net/board/view/35229

�ʱ�ȭ�� ����� �� ���༭ �ϳ��� ����ϸ� ���� �����µ�,
���� �׽�Ʈ���̽��� ����ϸ� ���� �� ���Դ�.
vector ���� �ʱ�ȭ �ݵ�� �����ֱ�
+ priority queue �ʱ�ȭ�� �����־��µ�, clear �޼ҵ尡 ��� �Ź� ����������Ѵ�. 
���� �Խ����� �������� �ݷʵ�δ� ã�� �� ���� ���׿���.
��û ���� �׽�Ʈ���̽��� �־���� ã���� �� 
+ ���� �Խ����� �ݷʵ�δ� ã�� �� ������ ������ �־���.
find_shortest �Լ����� if �� üũ�� ���� ������
���� ������ ���� ��찡 ����� ������ ���δ�. 
�Ʒ� ��ǲ ������� ������� ���� ��ǲ���� ������ �Ǵ� �� �߰��Ͽ���. 

���� �Խ����� ���� �ִ� ��� Ž���� bfs �� �� ����� ������,
���� ����Ž�� ���� �ʾƵ� ���ͽ�Ʈ��� �����ϴ�. 

��ǲ ������
https://www.acmicpc.net/board/view/50647 

23-04-09 Ʋ�Ƚ��ϴ�
1. find_shortest �� �� if �� �ʿ��� ���� ��Ȯ�� ���� �� �� 
=> ���ѷ����� �� �������, �Է��� ��û Ŀ���� ��͸� �ʹ� ���� ���� ��찡 ���� �� ���� ������ ���δ�.
�Ȱ��� ������ ����̰� �ݺ��ؼ� ���� ������ �� �� ���� ���̴�. 
2. Ʋ������ dist[0] �� �ƴ� dist[S] �� 0 ���� �����ؾ��ߴ�. 

23-04-12 �¾ҽ��ϴ� 
*/

// ���� Ǯ��
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
		cin >> S >> D; // ������, ������ (0~N-1) 
		
		// �ʱ�ȭ 
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

		// �ִ� ��� Ž�� 
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
		
		// �ִܰ���� path �� ���鼭 block üũ
		find_shortest(D, S);

		// block �� ���ؼ� ������ �ִ� ��� Ž�� 
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

// Ʋ�� Ǯ�� (dist[0] �ʱ�ȭ �Ǽ�) 
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
		cin >> S >> D; // ������, ������ (0~N-1) 
		
		// �ʱ�ȭ 
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

		// �ִ� ��� Ž�� 
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
		
		// �ִܰ���� path �� ���鼭 block üũ
		find_shortest(D, S);

		// block �� ���ؼ� ������ �ִ� ��� Ž�� 
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

// Ʋ�� Ǯ��
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
		cin >> S >> D; // ������, ������ (0~N-1) 
		
		// �ʱ�ȭ 
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

		// �ִ� ��� Ž�� 
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
		
		// �ִܰ���� path �� ���鼭 block üũ
		find_shortest(D, S);

		// block �� ���ؼ� ������ �ִ� ��� Ž�� 
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

// �߸� § Ǯ��
// ���ͽ�Ʈ�� ������ �ִ� ��θ� 1���� ã�� ���� �ƴ�
// ���� ��θ� �� Ȯ���� �� �־���� 
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
	// ��������Ʈ
	ios::sync_with_stdio(0);
	cin.tie(0);
	while (1) {
		cin >> N >> M;
		if (N == 0 && M == 0) break;
		cin >> S >> D; // ������, ������ (0~N-1) 
		for (int i = 0; i < M; ++i) {
			cin >> U >> V >> P;
			edge[U].push_back(make_pair(V, P));
		}
		// �������� 0 
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
		// path �� ���鼭 block üũ
		int node = path[D];
		while (node != S && node != -1) {
			block[node] = 1;
			node = path[node];
		}
		if (node == -1) {
			cout << -1 << '\n';
			continue;
		}
		// block �� ���ؼ� ���ͽ�Ʈ��
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
