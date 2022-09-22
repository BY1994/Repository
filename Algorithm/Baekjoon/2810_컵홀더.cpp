#include <stdio.h>

#define HOLDER (1)
#define SEAT (2)
#define DELETE (0)

char seats[51];
char theater[200];
int s;
int t;

int main(void)
{
	int N;
	int ans = 0;

	scanf("%d", &N);
	scanf("%s", seats);
	
	theater[t++] = HOLDER;
	
	while (s < N) {
		if (seats[s] == 'S') {
			theater[t++] = SEAT;
			theater[t++] = HOLDER;
			s++;
		}
		else {
			theater[t++] = SEAT;
			theater[t++] = SEAT;
			theater[t++] = HOLDER;
			s += 2;
		}
	}
	
	for (int i = 1; i < t; i++) {
		if (theater[i] == SEAT) {
			if (theater[i-1] == HOLDER) {
				theater[i-1] = theater[i] = DELETE;
				ans++;
			} else if (theater[i+1] == HOLDER) {
				theater[i+1] = theater[i] = DELETE;
				ans++;
			}
		}
	}
	
	printf("%d\n", ans);

	return 0;
}
