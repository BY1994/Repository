/*
5568 카드 놓기

Brute Force

메모리 제한이 256 MB 인데,
char 로 모든 수 체크를 하면 메모리 제한 안에 들어올 수 있어서
수 체크할 배열을 두고 간단하게 풀이하였다. 

(풀고 나서 문제 분류를 보니 해시를 사용한 집합과 맵이 있었다)

다른 사람 풀이를 보니
1. 어차피 최대 for 문 깊이가 4개라서 2중 ~ 4 중 포문으로 모든 경우를 만든 다음에
만들어진 string 결과를 sort 하여서 다른 값이 나오면 ++ 시켰다.
=> 결과를 check 배열로 두는 것보다 sorting 하고 체크하는게 메모리를 훨씬 덜 먹어서 좋을 것 같다. 
https://www.acmicpc.net/source/23311425

2. Python 은 단순히 permutation 을 다 생성한 후에 set 함수로 처리하면 끝난다. 
https://www.acmicpc.net/source/7270625

(Python 코드) 
import sys
import itertools

n,k,*c = map(int, sys.stdin.readlines())
c = list(map(str, c))

x = list()

for y in list(itertools.permutations(c,k)):
    x.append("".join(y))

print(len(set(x)))
*/
#include <stdio.h>

int n, k, ans;
int cards[10][2];
int visited[10];
char check[100000000];

void find(int depth, int num) {
	if (depth == k) {
		if (!check[num]) {
			check[num] = 1;
			ans++;
		}
		return;	
	}
	for (int i = 0; i < n; i++) {
		if (visited[i]) continue;
		visited[i] = 1;
		find(depth+1, num * cards[i][1] + cards[i][0]);
		visited[i] = 0;
	}
}

int main(void)
{
	scanf("%d", &n);
	scanf("%d", &k);
	for (int i = 0; i < n; i++) {
		scanf("%d", &cards[i][0]);
		if (cards[i][0] / 10) cards[i][1] = 100;
		else cards[i][1] = 10;
	}
	for (int i = 0; i < n; i++) {
		visited[i] = 1;
		find(1, cards[i][0]);
		visited[i] = 0;
	}
	printf("%d\n", ans);
	return 0;
}
