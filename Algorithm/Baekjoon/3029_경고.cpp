/*
3029 ��� 

// (1) time2 - time1
// (2) 24:00:00 - time1 + time2
�̹Ƿ� time2 - time1 �� ������ 

�ݷ�
������ ������... ������ �־���.
"(�����̴� ��� 1�ʸ� ��ٸ���, ���ƾ� 24�ð��� ��ٸ���.)" 
https://www.acmicpc.net/board/view/72187
�� �ڵ忡 ��ȣ �ϳ��� ������ �ݷʿ���
00:00:00
00:00:00
����: 24:00:00
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
