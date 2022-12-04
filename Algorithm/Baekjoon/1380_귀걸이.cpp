/*
1380 귀걸이

문자열 

2022.11.26

fgets 로 변경 => 출력초과
초기화 넣은 scanf("%[^\n]") 로 변경 => 틀렸습니다 
status 0 초기화 추가 => 틀렸습니다 

계속 틀렸던 이유는 이름 출력 뒤에 엔터를 넣지 않았기 때문 
*/

#include <stdio.h>

char name[101][61];
int status[101];

int main(void)
{
	int n, id;
	char letter;
	for (int tc = 1; ; tc++) {
		// 이름 받기
		scanf("%d", &n);
		if (n == 0) break;
		getchar();
		for (int i = 1; i <= n; ++i) {
			for (int j = 0; j < 61; ++j) name[i][j] = 0;
			scanf("%[^\n]", name[i]);
			getchar();
		}
		// 귀걸이 압수 & 반환
		for (int i = 1; i < 2*n; ++i) {
			scanf("%d %c", &id, &letter);
			if (status[id]) status[id]--;
			else status[id]++;
			getchar();
		}
		// 처리되지 못한 귀걸이 찾기
		for (int i = 1; i <= n; ++i) {
			if (status[i]) {
				printf("%d %s\n", tc, name[i]);
				status[i] = 0;
				break;
			}
		}
	}
	
	return 0;
}

// 출력초과
#if 0
#include <stdio.h>

char name[101][61];
int status[101];

int main(void)
{
	int n, id;
	char letter;
	for (int tc = 1; ; tc++) {
		// 이름 받기
		scanf("%d", &n);
		if (n == 0) break;
		getchar();
		for (int i = 1; i <= n; ++i) {
			fgets(name[i], 61, stdin);
			//scanf("%[^\n]", name[i]);
			//getchar();
		}
		// 귀걸이 압수 & 반환
		for (int i = 1; i < 2*n; ++i) {
			scanf("%d %c\n", &id, &letter);
			//getchar();
			if (status[id]) status[id]--;
			else status[id]++;
		}
		// 처리되지 못한 귀걸이 찾기
		for (int i = 1; i <= n; ++i) {
			if (status[i]) {
				printf("%d %s", tc, name[i]);
				break;
			}
		}
	}
	
	return 0;
}
#endif
