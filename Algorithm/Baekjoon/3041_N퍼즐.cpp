/*
3041 N 퍼즐 

원래 자리와 떨어진 자리의 맨해튼 거리들 합 
*/

#include <stdio.h>

char puzzle[4][4];
struct location{
	int x;
	int y;
}item[128];

void init(void)
{
	item['A'] = {0, 0};
	item['B'] = {0, 1};
	item['C'] = {0, 2};
	item['D'] = {0, 3};
	item['E'] = {1, 0};
	item['F'] = {1, 1};
	item['G'] = {1, 2};
	item['H'] = {1, 3};
	item['I'] = {2, 0};
	item['J'] = {2, 1};
	item['K'] = {2, 2};
	item['L'] = {2, 3};
	item['M'] = {3, 0};
	item['N'] = {3, 1};
	item['O'] = {3, 2};
}

int abs(int x){
	return (x > 0) ? x : -x;
}
int main(void)
{
	int ans = 0;
	init();
	for (int i = 0; i < 4; ++i) {
		scanf("%s", puzzle[i]);
	}
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (puzzle[i][j] == '.') continue;
			ans += abs(item[puzzle[i][j]].x - i);
			ans += abs(item[puzzle[i][j]].y - j);
		}
	}
	printf("%d\n", ans);
	return 0;
}
