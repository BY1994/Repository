/*
1497 기타리스트 (틀렸습니다) 

brute force + bitmasking

처음에 생각한 풀이 잘못됨 
1. 서로 배타적인 것끼리만 합칠 수 있음 
2. 모든 곡을 다 연주하지 않아도 됨. 최대값만 만들면 됨 

여전히 틀렸는데... 왜 틀렸는지 찾지 못함 
*/

#include <stdio.h>
#define MAX_VALUE (100)
int N, M;
int min = MAX_VALUE;
int count;
unsigned long long spec[51];
int songs[51];
char pos[51];
char name[51];

void dfs(int cur, int depth, unsigned long long visited, int cnt) {
	// 1. find min
	if (count < cnt) {
		min = depth;
		count = cnt;
	} else if (count == cnt) {
		if (min > depth) min = depth;
	}
	
	// 2. exit recursive func
	if (depth == N) return;
	
	// 3. next recursive func
	for (int i = cur+1; i < N; ++i) {
		// do not overlap!
		if (visited & spec[i]) continue;
		dfs(i, depth+1, visited | spec[i], cnt + songs[i]);
	}
}

int main(void) {
	// 1. get input
	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; ++i) {
		scanf("%s %s", name, pos);
		for (int j = 0; j < M; ++j) {
			spec[i] <<= 1ULL;
			if (pos[j] == 'Y') {
				spec[i] |= 1ULL;
				songs[i]++;
			}
		}
	}

	// 2. dfs
	for (int i = 0; i < N; ++i)
		dfs(i, 1, spec[i], songs[i]);

	// 3. print answer
	if (count) printf("%d\n", min);
	else printf("-1\n");

	return 0;
}

// 예제도 틀림
// 단순 BFS 라고 생각함 
#if 0
#include <stdio.h>
#define MAX_VALUE (100)
int N, M;
int min = MAX_VALUE;
unsigned long long max_visit;
unsigned long long spec[51];
char pos[51];
char name[51];
int flag;

void dfs(int cur, int depth, unsigned long long visited) {
	// 1. find min
	if (visited == max_visit && depth < min) {
		min = depth;
		flag = 1;
		return;
	}
	
	// 2. exit recursive func
	if (depth == N || flag == 1) return;
	
	// 3. next recursive func
	for (int i = cur+1; i < N; ++i)
		dfs(i, depth+1, visited | spec[i]);
}

int main(void) {
	// 1. get input
	scanf("%d %d", &N, &M);
	max_visit = (1ULL << (unsigned long long)M) - 1ULL;

	for (int i = 0; i < N; ++i) {
		scanf("%s %s", name, pos);
		for (int j = 0; j < M; ++j) {
			spec[i] <<= 1ULL;
			if (pos[j] == 'Y') spec[i] |= 1ULL;
		}
	}

	// 2. dfs
	for (int i = 0; i < N; ++i)
		dfs(i, 1, spec[i]);

	// 3. print answer
	if (min == MAX_VALUE) printf("-1\n");
	else printf("%d\n", min);

	return 0;
}
#endif
