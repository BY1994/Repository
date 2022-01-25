"""
10812 바구니 순서 바꾸기
"""

N, M = map(int, input().split())
basket = list(range(1, N+1))
for _ in range(M):
    i, j, k = map(int, input().split())
    basket[i-1:j] = basket[k-1:j]+basket[i-1:k-1]

print(*basket,sep= ' ')


# https://www.acmicpc.net/source/671213
# C 예시
"""
#include <stdio.h>
#include <string.h>

int n, m;
char s[105];

void swap(int begin, int mid, int end);

int main() {
	int i, begin, end, mid;

	scanf("%d %d", &n, &m);
	for(i = 0; i < n; ++i)
		s[i] = 1 + i;
	while(m--) {
		scanf("%d %d %d", &begin, &end, &mid);
		swap(begin - 1, mid - 1, end - 1);
	}
	for(i = 0; i < n; ++i)
		printf("%d ", s[i]);
	puts("");
	return 0;
}

void swap(int begin, int mid, int end) {
	char tmpA[105], tmpB[105];
	int lenA = mid - begin, lenB = end - mid + 1;

	strncpy(tmpA, s + begin, lenA);
	strncpy(tmpB, s + mid, lenB);
	strncpy(s + begin, tmpB, lenB);
	strncpy(s + begin + lenB, tmpA, lenA);
}
"""
