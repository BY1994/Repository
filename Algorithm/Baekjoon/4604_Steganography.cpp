/*
4604 Steganography

비트마스킹, 문자열
스페이스바의 개수가 홀수개면 0 짝수개면 1 로 판단 
*/

#include <stdio.h>
char tbl[32];
void init(void) {
    tbl[0] = ' ';
    for (int i = 1; i <= 26; ++i) {
        tbl[i] = 'A'+i-1;
    }
    tbl[27] = '\'';
    tbl[28] = ',';
    tbl[29] = '-';
    tbl[30] = '.';
    tbl[31] = '?';
}

int main(void)
{
	int size = 0;
	int cur = 0;
	int space = 0;

    init();
    while (1) {
        char text[81] = {0};
        scanf("%[^\n]", text);
        getchar();
        if (text[0] == '#') break;
        if (text[0] == '*') {
        	if (size > 0)  {
				printf("%c", tbl[cur << (5-size)]);
			}
        	size = cur = space = 0;
        	printf("\n");
		} else {
			for (int i = 0; text[i]; ++i) {
				if (text[i] == ' ') space++;
				else {
					if (space == 0) continue;
					cur <<= 1;
					cur |= (space+1)%2;
					size++;
					space = 0;
				}

				if (size >= 5) {
					printf("%c", tbl[cur]);
					size = cur = 0;
				}
			}
		}
    }

    return 0;
}
