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
- �������� ���ķ� �����ϴ� �ɷδ� �� �� �� 
- benefit �� ū �� ������ �������! 
ó���� �� benefit ���̵� �����س��Ⱑ �������. 

5) �ٸ� ������ ����ؾ��� ���� �߰� 
count ������ ���� �� �� ���� ���� ���� ����ؾ���
(�̰� �Ϻη� ������� �ʾҴµ� �ڵ忡�� for �� ��ȸ�� ������� �ؼ� �ݿ���) 

2023.03.26 Ʋ�Ƚ��ϴ� 
2023.03.28 �¾ҽ��ϴ� 
*/

#include <stdio.h>
#include <string.h>

char num[51][51];
int benefit[100][37];
int sorted_idx[37];
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

void sum_input(void){
	// benefit for each num
	for (int i = 0; i < N; ++i) {
		for (int j = length[i]-1; j >= 0; --j){
		    int num_input = str2num(num[i][j]);
			ans[length[i]-1-j] += num_input;
			benefit[length[i]-1-j][num_input] += 35 - num_input;
		}
	}

	// carry
    for (int n = 0; n < 36; ++n) {
        for (int i = 0; i < 90; ++i) {
            benefit[i+1][n] += benefit[i][n] / 36;
            benefit[i][n] %= 36;
        }
    }
}

void sort(void){
    // �̵��� ū ������� ����
    for (int i = 0; i < 36; ++i) sorted_idx[i] = i;
    for (int i = 0; i < 36; ++i) {
        for (int j = i+1; j < 36; ++j) {
            for (int k = 90; k >= 0; --k) {
                if (benefit[k][sorted_idx[i]] > benefit[k][sorted_idx[j]]) {
                    break;
                }
                else if (benefit[k][sorted_idx[i]] < benefit[k][sorted_idx[j]]) {
                    int temp = sorted_idx[j];
                    sorted_idx[j] = sorted_idx[i];
                    sorted_idx[i] = temp;
                    break;
                }
            }
        }
    }
}

void sum_K(void) {
    // K �� ��ŭ �����ֱ�
    for (int i = 0; i < K; ++i) {
        for (int j = 0; j < 90; ++j) {
            ans[j] += benefit[j][sorted_idx[i]];
        }
    }
    // carry
    for (int i = 0; i < 90; ++i) {
        ans[i+1] += ans[i] / 36;
        ans[i] %= 36;
    }
}

void print_ans(void) {
	int ans_size = 99;

	while (ans_size >= 0 && ans[ans_size] == 0) ans_size--;
	if (ans_size < 0) {
		printf("0\n");
		return;
	}
	for (int i = ans_size; i >= 0; --i)
		printf("%c", num2str(ans[i]));
	printf("\n");
}

int main(void) {
	get_input();
	sum_input();
	sort();
	sum_K();
	print_ans();
	return 0;
}

// 2023.03.26 Ʋ�� �ڵ�
#if 0 
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
#endif

// ���� �ڵ� 
// https://www.acmicpc.net/source/58261884
#if 0
#include <cstdio>
#include <algorithm>
using namespace std;

class bigInt {
public:
    int buf[55];
    int size;
    void init(void) {
        size = 0;
        for (int i = 0; i < 55; ++i) {
            buf[i] = 0;
        }
    }
    bigInt() {
        init();
    }
    int toDecimal(char c) {
        if (c >= '0' && c <= '9') {
            return c - '0';
        }
        return c - 'A' + 10;
    }
    bigInt& operator=(char *str) {
        init();
        int len = 0;
        while (str[len] != '\0') len++;
        for (int i = len - 1; i >= 0; --i) {
            buf[size++] = toDecimal(str[i]);
        }
        return (*this);
    }
    bigInt& operator=(bigInt other) {
        init();
        for (int i = 0; i < other.size; ++i) {
            buf[i] = other.buf[i];
        }
        size = other.size;
        return (*this);
    }
    bool operator<(bigInt &other) {
        if (size != other.size)
            return size < other.size;
        bool ret = false;
        for (int i = size - 1; i >= 0; --i) {
            if (buf[i] == other.buf[i]) continue;
            if (buf[i] < other.buf[i]) {
                ret = true;
                break;
            } else {
                ret = false;
                break;
            }
        }
        return ret;
    }
    bigInt& operator+=(bigInt &other) {
        int len = (size > other.size) ? size : other.size;
        bool carry = false;
        for (int i = 0; i < len; ++i) {
            buf[i] += other.buf[i];
            if (buf[i] >= 36) {
                buf[i + 1] += (buf[i] / 36);
                buf[i] %= 36;
                if (i + 1 >= len) carry = true;
            }
        }
        if (carry) len++;
        size = len;
        return (*this);
    }
    char toChar(int num) {
        if (num >= 0 && num <= 9) {
            return num + '0';
        }
        return num - 10 + 'A';
    }
    void toString(void) {
        if (size == 0) {
            printf("0\n");
            return;
        }
        for (int i = size - 1; i >= 0; --i) {
            printf("%c", toChar(buf[i]));
        }
        printf("\n");
    }
};

int N, K;
bigInt SCORE[36];
int main(void) {
    scanf("%d", &N);
    bigInt sum, val;
    for (int i = 0; i < N; ++i) {
        char input[51]; scanf("%s", input);
        val = input; sum += val;
        for (int j = 0; j < val.size; ++j) {
            int d = val.buf[j];
            int temp = 35 - d;
            bigInt diff;
            diff.buf[j] = temp;
            if (temp != 0) diff.size = j + 1;
            SCORE[d] += diff;
        }
    }
    scanf("%d", &K);
    sort(SCORE, SCORE + 36);
    for (int i = 35; i > 35 - K; --i) {
        sum += SCORE[i];
    }
    sum.toString();
    return 0;
}
#endif

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
