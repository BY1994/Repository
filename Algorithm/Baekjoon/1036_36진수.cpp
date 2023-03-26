/*
1036 36 ���� 

���ڵ����� �Ǽ��ߴ� �κ�
1) sum�� carry ����� �� carry �� �� �̻� ������ ���� ������
while �� ���ȴµ�, carry �� ������ �ʾƵ� �� ���� ���� ���� ���ɼ��� ����
��ü�� for�� ��ȸ�ϴ� ������ ���� 
[����]
1
Z
Z
0 
2) count �� �� �ε����� �ݴ�� �־�� �Ѵٴ� ���� ��� �� �� 
(for �� ��ȸ�� �ݴ�� ��) 
[����]
1
HELLO
2 
3) substitute �Լ����� K �� 0 �� �� ���, while ���� Ż����Ѿ��ϴµ�
if �� üũ���� �־ ���� ������ ������ 
4) �ݷʰ� �ִ�. �ڵ� �ؿ� �߰���
�ݷʿ� ���� ����
https://www.acmicpc.net/board/view/51885 
�ܼ��� �� �տ������� ġȯ�ϴ� �׸���δ� �� ������ Ǯ �� ����,
��ü���� ���� �� ����ؾ��Ѵ�! 

2023.03.26 Ʋ�Ƚ��ϴ� 
*/

#include <stdio.h>
#include <string.h>

char num[51][51];
int num36[51][51]; // sum �� ���� ������ 
int count[51][37]; // num36 �� ���� �ε��� ��� 
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
	for (int j = 51; j >= 0; --j) { // max(length[]) �� ���� ���� 
		if (K <= 0) break;
		int flag = 0;
		// ���� ���� �ڸ����� ���� �����ϴ� ������� ��ü 
		while (flag == 0 && K > 0) {
			int max_ind, max_value = 0;
			flag = 1;
			for (int k = 0; k < 35; ++k) { // Z �������� ���� 
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

// �ݷ� ���� 
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
