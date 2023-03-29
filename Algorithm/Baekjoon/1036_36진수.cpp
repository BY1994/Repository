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
- 내림차순 정렬로 구현하는 걸로는 안 될 것 
- benefit 도 큰 수 연산을 해줘야함! 
처음에 이 benefit 아이디어를 생각해내기가 어려웠다. 

5) 다른 가능한 고려해야할 문제 발견 
count 개수가 같을 때 더 작은 수를 먼저 고려해야함
(이건 일부러 고려하지 않았는데 코드에서 for 문 순회를 순서대로 해서 반영됨) 

2023.03.26 틀렸습니다 
2023.03.28 맞았습니다 
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
    // 이득이 큰 순서대로 정렬
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
    // K 개 만큼 더해주기
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

// 2023.03.26 틀린 코드
#if 0 
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
#endif

// 샘플 코드 
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
