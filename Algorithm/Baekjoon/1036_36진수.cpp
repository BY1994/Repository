/*
1036 36 진수 

손코딩에서 실수했던 부분
1) sum의 carry 계산할 때 carry 가 더 이상 생기지 않을 때까지
while 을 돌렸는데, carry 가 생기지 않아도 그 다음 수는 생길 가능성이 있음
전체를 for로 순회하는 것으로 변경 
[예제]
1
Z
Z
0 
2) count 할 때 인덱스를 반대로 넣어야 한다는 것을 고려 안 함 
(for 문 순회를 반대로 함) 
[예제]
1
HELLO
2 
3) substitute 함수에서 K 가 0 이 된 경우, while 문을 탈출시켜야하는데
if 문 체크에만 넣어서 무한 루프가 생겼음 
4) 반례가 있다. 코드 밑에 추가함
반례에 대한 설명
https://www.acmicpc.net/board/view/51885 
단순히 맨 앞에서부터 치환하는 그리디로는 본 문제를 풀 수 없고,
전체적인 것을 다 고려해야한다! 

2023.03.26 틀렸습니다 
*/

#include <stdio.h>
#include <string.h>

char num[51][51];
int num36[51][51]; // sum 을 위해 뒤집힘 
int count[51][37]; // num36 과 같은 인덱스 사용 
int ans[100];
int length[51];
int changed[37];
int N, K;

int str2num(char x) {
	if ('0' <= x && x <= '9') return x - '0';
	return x - 'A' + 10;
}

char num2str(int x) {
	if (0 <= x && x <= 9) return x + '0';
	return x - 10 + 'A';
}

void get_input(void){
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%s", num[i]);
		length[i] = strlen(num[i]);
	}
	scanf("%d", &K);
}

void count_num(void){
	for (int i = 0; i < N; ++i) {
		for (int j = length[i]-1; j >= 0; --j){
			num36[i][length[i]-1-j] = str2num(num[i][j]);
			count[length[i]-1-j][num36[i][length[i]-1-j]]++;
		}
	}
}

void substitute(void){
	for (int j = 51; j >= 0; --j) { // max(length[]) 로 개선 가능 
		if (K <= 0) break;
		int flag = 0;
		// 가장 높은 자리에서 많이 등장하는 순서대로 대체 
		while (flag == 0 && K > 0) {
			int max_ind, max_value = 0;
			flag = 1;
			for (int k = 0; k < 35; ++k) { // Z 전까지만 포함 
				if (changed[k]) continue;
				if (max_value < count[j][k]) {
					flag = 0;
					max_value = count[j][k];
					max_ind = k;
				}
			}
			if (max_value) {
				changed[max_ind] = 1;
				K--;
			}
		}
	}
}

void sum(void) {
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < length[i]; ++j) {
			if (changed[num36[i][j]]) ans[j] += 35;
			else ans[j] += num36[i][j];
		}
	}
	
	for (int i = 0; i < 100; ++i) {
		ans[i+1] += ans[i]/36;
		ans[i] %= 36;
	}
}

void print_ans(void) {
	int ans_size = 99;

	while (ans_size >= 0 && ans[ans_size] == 0) ans_size--;
	if (ans_size <= 0) {
		printf("0\n");
		return;
	}
	for (int i = ans_size; i >= 0; --i)
		printf("%c", num2str(ans[i]));
	printf("\n");
}

int main(void) {
	get_input();
	count_num();
	substitute();
	//for (int i = 0; i < 37; ++i) {
	//	printf("%d ", count[51][i]);
	//}
	//printf("\n");
	sum();
	print_ans();
	return 0;
}

// 반례 모음 
// https://www.acmicpc.net/board/view/69763
/*
50
XWW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
WW
1
ans: 2AYM
*/
