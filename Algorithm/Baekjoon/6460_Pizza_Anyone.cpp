/*
6460 Pizza Anyone

요청 최대 개수에 대한 설명이 없음 
+A+B+C+D-E-F-G-H;
-A-B+C+D-E-F+G+H;
-A+B-C+D+F-G+H;
.
+A+B+C+D-E-F-G-H;
-A-B+C+D-E-F+G+H;
-A+B-C+D+F-G+H;
.

틀렸던 가장 큰 이유
토핑 개수를 세서 16 개라는 걸 보고 짰어야하는데,
문제에 12라는 숫자 대충 보고 토핑이 12개라고 생각하고 짠 것 

flag break 조건 제대로 신경 안 쓴 것
가독성 좋게 짜는 법을 고민해야할 듯 
*/

#include <stdio.h>

char request[30];
int requests[100][2]; // like vs. hate (12 lists) 

int main(void) {
	int flag = 0;
	int r;
	while (1) { // TC
		for (r = 0; ; ++r) {
			if (scanf("%s", request) == EOF) {
				flag = 1;
				break;	
			}
			if (request[0] == '.') break; 
			requests[r][0] = requests[r][1] = 0;
			for (int i = 1; request[i]; i += 2) {
				if (request[i-1] == '+') {
					requests[r][0] |= 1 << (request[i]-'A');
				} else {
					requests[r][1] |= 1 << (request[i]-'A');
				}
			}
		}

		if (flag == 1) break; // 맨 밑에 두면 출력 하나 더 한 후에 break 될 것 

		// CELP = 0b1000100000010100 (34836) 1<< 12 는 4096 
		int satisfy = 1; int ans = 0;
		for (int c = 0; c < (1 << 16); ++c) {
			satisfy = 1;
			for (int j = 0; j < r; ++j) {
				if (((c & requests[j][0]) == 0) && (((~c) & requests[j][1]) == 0) ) {
					satisfy = 0;
					break;
				}
			}
			if (satisfy) {
				ans = c;
				break;
			}
		}
		// 모든 j 를 다 통과하면 topping 으로 출력 
		if (satisfy) {
			printf("Toppings: ");
			for (int j = 0; j < 16; ++j) {
				if ((ans >> j) & 1) printf("%c", 'A'+j);
			}
			printf("\n");
		} else printf("No pizza can satisfy these requests.\n");

	}
	return 0;
}
