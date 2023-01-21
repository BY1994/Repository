/*
3029 경고 

// (1) time2 - time1
// (2) 24:00:00 - time1 + time2
이므로 time2 - time1 은 공통임 

반례
문제의 잔인한... 함정이 있었다.
"(정인이는 적어도 1초를 기다리며, 많아야 24시간을 기다린다.)" 
https://www.acmicpc.net/board/view/72187
내 코드에 등호 하나로 갈리는 반례였음
00:00:00
00:00:00
정답: 24:00:00
*/

#include <stdio.h>

int main(void) {
	int h1, m1, s1, h2, m2, s2, time1, time2;
	scanf("%d:%d:%d", &h1, &m1, &s1);
	scanf("%d:%d:%d", &h2, &m2, &s2);
	time1 = h1*3600 + m1*60 + s1;
	time2 = h2*3600 + m2*60 + s2;
	int diff = time2-time1;
	if (diff <= 0) diff += 24*3600;
	printf("%02d:%02d:%02d\n", diff/3600, (diff%3600)/60, diff%60);
	return 0;
}
