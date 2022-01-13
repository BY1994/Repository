#include <stdio.h>

int d[510];
int a[510];

int main(void)
{
	int n, l, k;
	int ans = 0;
	scanf("%d %d %d", &n, &l, &k);
	for (int i = 0; i < n; i++) scanf("%d", &d[i]);
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
	d[n] = l;

	for (int i = 0; i < k; i++) {
		int dist = -1;
		int ind, cur;
		for (int j = 1; j < n; j++) {
			if (a[j] <= a[j-1]) continue;
			cur = (d[j+1]- d[j])*a[j];

			if (cur > dist) dist = cur, ind = j;
		}
		if (dist < 0) break;
		a[ind] = a[ind-1];
	}
	
	for (int i = 0; i < n; i++) {
		ans += (d[i+1]-d[i])*a[i];
	}
	
	printf("%d\n", ans);
	return 0;
}
