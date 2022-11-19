/*
1525 ���� 

BFS & Hash

100% ���� Ʋ���� ����
(ó������ ������ ���) 
https://www.acmicpc.net/board/view/47368

1 2 3
4 5 6
7 8 0
*/

#include <stdio.h>
#include <unordered_map>
#include <queue>

using namespace std;

int board[3][3];
int pos[3][3] = {{100000000,10000000,1000000},
				{100000,10000,1000},
				{100,10,1}};
struct _queue{
	int x;
	int y;
	int cur_map;
	int dis;
}; 

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main(void)
{
	int cur_map = 0;
	int X, Y;
	unordered_map <int, int> hash_table;
	queue <struct _queue> q;

	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 3; ++j) {
			scanf("%d", &board[i][j]);
			cur_map *= 10;
			cur_map += board[i][j];
			if (board[i][j] == 0) {
				X = i, Y = j;
			}
		}
	}
	hash_table[cur_map] = 1;
	q.push({X, Y, cur_map, 0}); // �̵�Ƚ�� 
	while (!q.empty()) {
		struct _queue cur = q.front();
		q.pop();
		// ���� ������ Ȯ���ϱ� (���ۺ��� ������ �ݷʰ� �־� ��ġ �ű�)
		if (cur.cur_map == 123456780) {
		    printf("%d\n", cur.dis);
			return 0;
		}
		for (int d = 0; d < 4; ++d) {
			int nx = cur.x + dx[d];
			int ny = cur.y + dy[d];
			if (nx < 0 || ny < 0 || nx > 2 || ny > 2) continue;
			// �� �ٽ� ���ϰ�
			int next_map = cur.cur_map;
			int val = (next_map / pos[nx][ny]) % 10;
			next_map += val*pos[cur.x][cur.y];
			next_map -= val*pos[nx][ny];
			// visited Ȯ���ϰ� ������ �ֱ� 
			if (hash_table.find(next_map) == hash_table.end()) {
				hash_table[next_map] = 1;
				q.push({nx, ny, next_map, cur.dis+1});
			}
		}
	}
	printf("-1\n");
	return 0;
}

// �ٸ� �ڵ�
// https://www.acmicpc.net/source/51670631
/*
#include <iostream>
#include <queue>
#include <string>
#include <map>
using namespace std;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };

int main() {

	int N = 3;
	int begin = 0;
	for (int i = 0; i<N; i++) {
		for (int j = 0; j<N; j++) {
			int tmp;
			cin >> tmp;
			if (tmp == 0) {
				tmp = 9;
			}
			begin = begin*10 + tmp;
		}
	}

	queue<int> q;
	map<int, int> dist;
	dist[begin] = 0;
	q.push(begin);
	while (!q.empty()) {
		int now = q.front(); q.pop();
		string now_str = to_string(now);
		int z = now_str.find('9');
		int x = z / 3;
		int y = z % 3;
		for (int k = 0; k<4; k++) {
			int nextX = x + dx[k];
			int nextY = y + dy[k];
			if (nextX >= 0 && nextX < N && nextY >= 0 && nextY < N) {
				string next = now_str;
				int tmp = next[x*3 + y];
				next[x * 3 + y] = next[nextX * 3 + nextY];
				next[nextX * 3 + nextY] = tmp;
				
				int next_num = stoi(next);
			//	cout << next_num << endl;
			//	cout << dist.count(next_num) << endl;
				if (dist.count(next_num) == 0) {
					dist[next_num] = dist[now] + 1;
					q.push(next_num);
				}
			}
		}
	}
	if ( dist.count(123456789) == 0) {
		cout << -1 << '\n';
	}
	else {
		cout << dist[123456789] << '\n';
	}
	return 0;
}
*/
