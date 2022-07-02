/*
1238 ��Ƽ

���ͽ�Ʈ�� 
C++ stl �ڵ� ����: https://yabmoons.tistory.com/364 
���� Ǯ�� �ڵ� ����: https://hyeo-noo.tistory.com/138 
�������� �켱���� ť�� ��� ������, �켱����ť �迭�� ���� �� �ֳ� �ϴٰ� ã�Ҵµ�,
�Ź� �ʱ�ȭ�� �ϸ� �Ǵ� �ſ���... 

�ð��� ���� Ǯ�̵��� ����, ó���� ���� �Է� ���� �� ���������ε� �����ϰ�,
���ͽ�Ʈ�� ���� �������� 2�� ���ȴ�.
�̷��� �ϸ� �ξ� �����ٰ� �ϴµ� ���� ��Ȯ�� ���ش� �� �ߴ�. 
*/

#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
const int INF = 1000000000;

int N, M, X;
vector<pair<int, int> > v[100001];
vector<int> dist;
int min_dist[1001];
int ans;

void dijkstra(int start){
	dist.clear();
	dist.resize(N+1, INF);
	
	dist[start] = 0;
	
	priority_queue<pair<int, int> > PQ;
	PQ.push(make_pair(0, start));
	
	while (!PQ.empty()) {		
		int cost = -PQ.top().first;
		int cur = PQ.top().second;
		PQ.pop();
		
		for (int i = 0; i< v[cur].size(); ++i) {
			int next = v[cur][i].first;
			int ncost = cost + v[cur][i].second;
			
			if (dist[next] > ncost) {
				dist[next] = ncost;
				PQ.push(make_pair(-ncost, next));
			}
		}
	}
}

int main(void) {
    scanf("%d %d %d", &N, &M, &X);

    for (int i = 0; i < M; ++i) {
        int a, b, c; scanf("%d %d %d", &a, &b, &c);
        v[a].push_back(make_pair(b, c));
    }
    
    for (int i = 1; i <= N; ++i) {
    	dijkstra(i);
		min_dist[i] = dist[X]; 	
	}

    dijkstra(X);

    for (int i = 1; i <= N; ++i) {
    	min_dist[i] += dist[i];
    	ans = max(ans, min_dist[i]);
    }

    printf("%d\n", ans);
    return 0;
}

