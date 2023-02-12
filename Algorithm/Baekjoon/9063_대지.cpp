/*
9063 대지 

구현, 기하학

기하학 태그로 검색한 문제인데 단순 최소 최대 문제였다. 
*/

#include <stdio.h>

inline int max(int a, int b) {
	return (a > b) ? a : b;
}
inline int min(int a, int b) {
	return (a > b) ? b : a;
}
inline int abs(int x) {
	return (x > 0) ? x : -x;
}

int main(void) {
	int N, x, y;
	int _minx = 10001, _miny = 10001;
	int _maxx = -10001, _maxy = -10001;

	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d %d", &x, &y);
		_minx = min(_minx, x);
		_maxx = max(_maxx, x);
		_miny = min(_miny, y);
		_maxy = max(_maxy, y);
	}
	printf("%d\n", abs((_maxx - _minx)*(_maxy - _miny)));
	return 0;
}
