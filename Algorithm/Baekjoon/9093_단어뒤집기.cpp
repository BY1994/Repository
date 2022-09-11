/*
9093 단어 뒤집기

stack 문제와 생긴게 비슷함 
 
띄어쓰기 포함해서 scanf 받는 방법
gets 사용 
https://isss.tistory.com/838
 
어셈으로 짠 사람도 있음...
https://www.acmicpc.net/source/25878863 
*/
#include <stdio.h>
char sentence[1001];

void rprint(int s, int e) {
	for (int i = e; i >= s; --i) {
		printf("%c", sentence[i]);
	}
	printf(" ");
}

int main(void)
{
	int tc, i, j;
	
	scanf("%d\n", &tc);
	while (tc--) {
		gets(sentence);
		for (i = 0; sentence[i];) {
			if (sentence[i] != ' ') {
				for (j = i; sentence[j] && sentence[j] != ' '; j++);
				rprint(i, j-1);
				i = j;
			} else i++;
		}
		printf("\n");
	}
	return 0;
}


#if 0 // 예제는 나왔는데 코드가 복잡해서 수정할 것 
#include <stdio.h>

int main(void)
{
	int tc, i, j;
	char sentence[1001];
	char saved[21];
	
	scanf("%d\n", &tc);
	while (tc--) {
		gets(sentence);
		for (i = 0; sentence[i];) {
			if (sentence[i] != ' ') {
				int s = 0;
				for (j = i; sentence[j] && sentence[j] != ' '; j++) {
					saved[s++] = sentence[j];
				}
				i = j;
				while (s) {
					printf("%c", saved[--s]);
				}
				printf(" ");				
			} else i++;
		}
		printf("\n");
	}
	return 0;
}
#endif

// 다른 풀이
// https://www.acmicpc.net/source/30050721 
#if 0
#include <unistd.h>
#define SZ (1320 << 10)

__libc_start_main() {
    char r[SZ], *p = r, *pp; read(0, r, SZ);
    for (; *p & 16; p++); pp = ++p;
    for (int i; (i = 0) || *p; p += i + 1) {
        while (p[++i] & 64);
        for (int j = 0; j < i - 1 - j; j++) {
            p[j] ^= p[i - 1 - j] ^= p[j] ^= p[i - 1 - j];
        }
    } write(1, pp, p - pp); _exit(0);
} main;
#endif
