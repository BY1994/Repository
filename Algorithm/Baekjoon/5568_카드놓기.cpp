/*
5568 ī�� ����

Brute Force

�޸� ������ 256 MB �ε�,
char �� ��� �� üũ�� �ϸ� �޸� ���� �ȿ� ���� �� �־
�� üũ�� �迭�� �ΰ� �����ϰ� Ǯ���Ͽ���. 

(Ǯ�� ���� ���� �з��� ���� �ؽø� ����� ���հ� ���� �־���)

�ٸ� ��� Ǯ�̸� ����
1. ������ �ִ� for �� ���̰� 4���� 2�� ~ 4 �� �������� ��� ��츦 ���� ������
������� string ����� sort �Ͽ��� �ٸ� ���� ������ ++ ���״�.
=> ����� check �迭�� �δ� �ͺ��� sorting �ϰ� üũ�ϴ°� �޸𸮸� �ξ� �� �Ծ ���� �� ����. 
https://www.acmicpc.net/source/23311425

2. Python �� �ܼ��� permutation �� �� ������ �Ŀ� set �Լ��� ó���ϸ� ������. 
https://www.acmicpc.net/source/7270625

(Python �ڵ�) 
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
