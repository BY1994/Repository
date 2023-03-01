/*
1388 바닥 장식 

구현, dfs

dfs 가 꼭 필요한가?
재귀는 사용할 수 있을 것 같은데 

- 일 때는 j 를 ++ 시켜도 되는데, (시간 단축도 있을 것) 
코드의 가독성을 위해서 그대로 뒀다. 
*/

#include <stdio.h>
int visited[51][51];
char floor[51][51];

int main(void) {
	int N, M, curx, cury;
	int count = 0;

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf(" %c", &floor[i][j]);
		}
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (visited[i][j]) continue;
			curx = i, cury = j;
			count++;
			if (floor[curx][cury] == '-'){
				while (floor[curx][cury] == '-') {
					visited[curx][cury] = 1;
					cury++;
				}				
			} else {
				while (floor[curx][cury] == '|') {
					visited[curx][cury] = 1;
					curx++;
				}				
			}
		}
	}
	printf("%d\n", count);
	return 0;
}

// c 언어 1등 풀이
// 풀이 방식은 비슷함 
#if 0
#include <unistd.h>
#define R_SIZE 10108

char r_buf[R_SIZE];
int r_pos = 0;

int read_i(void);

int main(void) {}

int __libc_start_main(void) {
    read(STDIN_FILENO, r_buf, R_SIZE);
    int N = read_i();
    int M = read_i();
    char (* table)[M + 1] = (char (*)[M + 1])&r_buf[r_pos];
    int x = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (table[i][j] == 'v') continue;
            if (table[i][j] == '|') {
                for (int k = 1; i + k < N; k++) {
                    if (table[i + k][j] == '|') table[i + k][j] = 'v';
                    else break;
                }
            } else {
                for (int k = 1; j + k < M; k++) {
                    if (table[i][j + k] == '-') table[i][j + k] = 'v';
                    else break;
                }
            }
            x++;
        }
    }
    char w_buf[5];
    int w_pos = 4;
    for (;;) {
        w_buf[w_pos] = (char)(x % 10 + '0');
        x /= 10;
        if(!x) break;
        w_pos--;
    }
    write(STDOUT_FILENO, w_buf + w_pos, 5 - w_pos);
    _exit(0);
}

int read_i(void) {
    char c;
    int n = 0;
    while ((c = r_buf[r_pos++]) != ' ' && c != '\n')
        n = n * 10 + c - '0';
    return n;
}
#endif
