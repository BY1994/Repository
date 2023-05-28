/*
6460 Pizza Anyone

��û �ִ� ������ ���� ������ ���� 
+A+B+C+D-E-F-G-H;
-A-B+C+D-E-F+G+H;
-A+B-C+D+F-G+H;
.
+A+B+C+D-E-F-G-H;
-A-B+C+D-E-F+G+H;
-A+B-C+D+F-G+H;
.

Ʋ�ȴ� ���� ū ����
���� ������ ���� 16 ����� �� ���� ®����ϴµ�,
������ 12��� ���� ���� ���� ������ 12����� �����ϰ� § �� 

flag break ���� ����� �Ű� �� �� ��
������ ���� ¥�� ���� ����ؾ��� �� 
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

		if (flag == 1) break; // �� �ؿ� �θ� ��� �ϳ� �� �� �Ŀ� break �� �� 

		// CELP = 0b1000100000010100 (34836) 1<< 12 �� 4096 
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
		// ��� j �� �� ����ϸ� topping ���� ��� 
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
