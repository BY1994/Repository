/*
19941 햄버거 분배

greedy 문제
왼쪽에서 먼저 최대한 먼 햄버거를 하나 고르면, 
오른쪽 상황을 고려하지 않아도 그게 항상 최적임이 보장되는 듯 하다. 
가능할 것 같아서 코드를 짜서 통과는 했지만 
정확한 증명은 어떻게 하는지 모르겠다 

코드를 짜다가 실수한 게 하나 있었는데,
햄버거를 하나 찾으면 바로 break 를 해야하는데 그걸 넣지 않아서
한 사람이 여러 햄버거를 먹도록 동작시켰었다. 

질문게시판에 글이 몇 개 있었는데 반례를 찾지 못했다.
아래는 답변한 목록이다. 
런타임 에러 해결
https://www.acmicpc.net/board/view/85375 
Try Catch 막힘
https://www.acmicpc.net/board/view/71099 
Python 에 음수 조건문으로 처리 안 해줌 (런타임 에러가 안 나서 못 찾았을 것) 
https://www.acmicpc.net/board/view/66505 
*/

#include <stdio.h>
int N, K, ans;
char table[20010];

int main(void) {
	scanf("%d %d", &N, &K);
	scanf("%s", table);
	for (int i = 0; i < N; i++) {
		if (table[i] == 'P') {
			for (int j = -K; j <= K; j++) {
				int next_i = i + j; 
				if (next_i < 0 || next_i >= N) continue;
				if (table[next_i] == 'H') {
					table[next_i] = 0;
					ans++;
					break;
				}
			}
		} 
	}
	printf("%d\n", ans);
	return 0;
}

