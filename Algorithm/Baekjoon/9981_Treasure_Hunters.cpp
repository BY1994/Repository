/*
9981 Treasure Hunters (fail)

모든 보물을 나눠줘야하는 듯 
보물 입장에서 사냥꾼을 선택하는 방식으로 가야할 듯 

START
5
3
42 500 350 700 100
250 200 500 1000 75
150 400 800 800 150
END

START
5
3
42 500 350 200 100
250 200 500 1000 75
150 400 800 800 150
END

START
5
3
500 500 350 200 100
250 200 500 1000 75
150 400 800 800 150
END
*/

// fail (2023.06.10) 
#if 0
#include <stdio.h>

char word[6];
int value[6][8];
int distribution[6];
int ans_distribution[6];
int max;
int ans;
int t, h;

void getmax(int hunter, int treasure, int state, int cur, int max, int min) { // current hunter, treasure state
	if (hunter == h) {
		printf("## max %d min %d\n", max, min);
		if (max - min < ans) {
			ans = max - min;
			for (int i = 0; i < h; ++i) ans_distribution[i] = distribution[i];
		}
		return;
	}
	if (treasure == t) {
		if (distribution[hunter] == 0) return; // no choice
		if (cur > max) max = cur;
		if (cur < min) min = cur;
		getmax(hunter+1, 0, state, 0, max, min);
		return;
	}
	getmax(hunter, treasure+1, state, cur, max, min);
	if ((state >> treasure) & 1) return;
	distribution[hunter] |= 1 << treasure;
	getmax(hunter, treasure+1, state | (1 << treasure), cur + value[hunter][treasure], max, min);
	distribution[hunter] &= ~(1 << treasure);
}

int main(void) {
	while (scanf("%s", word) != EOF) { // START
		max = 0;
		ans = 480000;
		scanf("%d", &t);
		scanf("%d", &h);
		for (int i = 0; i < h; ++i) {
			distribution[i] = 0;
			for (int j = 0; j < t; ++j) {
				scanf("%d", &value[i][j]);
			}
		}
		for (int i = 0; i < h; ++i) {
			getmax(i, 0, 0, 0, 0, 80000);
		}
		scanf("%s", word); // END
		for (int i = 0; i < h; ++i) {
			int count = 0;
			for (int j = 0; j < t; ++j) {
				if ((ans_distribution[i] >> j)&1) {
					printf("%d ", j+1);
					count += value[i][j];
				}
			}
			printf("%d\n", count);
		}
		printf("\n");
		printf("## %d\n", ans);
	}
	return 0;
}
#endif

