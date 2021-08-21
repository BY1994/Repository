/*
3954 brain f**k interpreter
1. %c 로 받는 경우 \n 개행문자가 같이 받아져서
input이 이상하게 받아진다. getchar() 를 사이에 넣고 해결
2. code max 범위 50000000 으로 한 게 edge case에 걸렸다.
1을 추가해서 반례를 맞췄다.
https://www.acmicpc.net/board/view/61124
Input :
2
65359 16 3
+[>+],...[[-],+]
999
65359 16 3
+[>+],[[-],+]+[]
999

Answer :
Terminates
Loops 14 15
3. Loops 기준 => 가장 최근 루프로 하면 안 됨
https://www.acmicpc.net/board/view/9096
무한루프에 해당하는 루프가 최근에 있던 루프라는 보장이 없습니다.
가령, +[+[-]] 같은 식의 중첩 루프를 생각해 보면 답은 바깥 루프지만, 우연히 5천만 번째 실행 중에 안쪽 루프 내용을 실행하고 있었다면 안쪽 루프를 답으로 출력해버릴 것입니다.
https://www.acmicpc.net/board/view/61103
Input
2
3 124 1
+[-[[>+[>----------------------------------[+++]<+]++++++++++++++++++++++++++[+]<+]----------------------------------[+]]++]
.
1 8 1
+[-[]++]
.

Output
Loops 1 123
Loops 3 4
*/

#include <stdio.h>

int msize;
int csize;
int isize;
unsigned int pointer;
unsigned int input_index;
unsigned int last_loop; /* last loop [ index */

unsigned char codes[4096];
unsigned char inputs[4096];
unsigned char memory[100010];
unsigned char jumps[4096];

int sets[2][4100]; /* 0: [ or ], 1: location */

void preprocess(void)
{
	int num = 0;
	for (int i = 0; i < csize; i++) {
		if (codes[i] == '[') {
			num++;
			sets[0][num] = i;
		}
		if (codes[i] == ']') {
			sets[1][num] = i;
			jumps[sets[0][num]] = sets[1][num];
			jumps[sets[1][num]] = sets[0][num];
			num--;
		}
	}
}

int do_code(int index)
{
	int ret = index + 1;
	if (codes[index] == '-') {
		memory[pointer] = (memory[pointer] + 256 - 1) % 256;
	}
	else if (codes[index] == '+') {
		memory[pointer] = (memory[pointer] + 1) % 256;
	}
	else if (codes[index] == '<') {
		pointer = (pointer + msize - 1) % msize;
	}
	else if (codes[index] == '>') {
		pointer = (pointer + 1) % msize;
	}
	else if (codes[index] == '[') {
		last_loop = index;
		if (memory[pointer] == 0) ret = jumps[index] + 1;
	}
	else if (codes[index] == ']') {
		if (memory[pointer] != 0) ret = jumps[index] + 1;
	}
	else if (codes[index] == ',') {
		if (input_index >= isize) {
			memory[pointer] = 255;
		}
		else {
			memory[pointer] = inputs[input_index++];
		}
	} // pass "."
	return ret;
}

void run(void)
{
	int max_code = 50000001;
	int index = 0;

	pointer = 0;
	input_index = 0;
	last_loop = 0;

	while (max_code--) {
		if (index >= csize) {
			printf("Terminates\n");
			return;
		}

		index = do_code(index);
	}
	printf("Loops %d %d\n", last_loop, jumps[last_loop]);
}

void init(void)
{
	scanf("%d %d %d", &msize, &csize, &isize);

	for (int i = 0; i < msize; i++) {
		memory[i] = 0;
	}
	for (int i = 0; i < csize; i++) {
		scanf(" %c", &codes[i]);
	}
	getchar();
	for (int i = 0; i < isize; i++) {
		scanf(" %c", &inputs[i]);
	}
	getchar();
}

int main(void)
{
	int tc;
	scanf("%d", &tc);
	for (int t = 0; t < tc; t++) {

		/* get input & init arrays */
		init();

		/* [[ ]] find sets */
		preprocess();

		/* start codes */
		run();
	}
}