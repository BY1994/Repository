#include <stdio.h>

int prev[150001];

int main(void)
{
	int t, n, dist;
	scanf("%d", &t);
	for (int T = 0; T < t; T++) {
		int ans = -1; // max
		int val;
		scanf("%d", &n);

		for (register int i = 0; i <= 150000; i++) {
			prev[i] = -1;
		}

		for (register int i = 0; i < n; i++){
			scanf("%d", &val);
			if (prev[val] < 0) prev[val] = i;
			else {
				dist = n-i + prev[val];
				prev[val] = i;
				if (ans < dist) ans = dist;
			}
		}
		printf("%d\n", ans);		
		 
	}
	return 0;
}
