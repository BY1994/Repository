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
4. infinite loop 안에 50000000 번 실행
terminate 후에도 50000000 번 실행되도록 바꿈

https://www.acmicpc.net/board/view/61124
Input
1
3 209 1
+[>+[>----------------------------------[+++]<+]++++++++++++++++++++++++++[+]<+],[-].+[-[[>+[>----------------------------------[+++]<+]++++++++++++++++++++++++++[+]<+]----------------------------------[+]]++]
1

Output
Loops 86 208

5. 무한루프 진입시 조건이 항상 동일하지 않음
무한루프 [ 로 돌아올 때 조건이 항상 똑같지 않다.
무조건 ++ 로 무한히 늘어날 수도 있음
=> 무한루프 체크한 걸 못 찾으면 가장 안쪽 루프에서 탈출 못하는 것

https://www.acmicpc.net/board/view/58310
===== 입력 =====
2
10 5 1
+[[]]
a
1 9 1
++[[++]+]
a

===== 출력 =====
Loops 2 3
Loops 3 6

6. 모든 반례 적용하고도 wrong
5번에서 무한루프가 항상 조건이 똑같지 않다는게 문제인 듯...

*/

#include <stdio.h>

int msize;
int csize;
int isize;
unsigned int pointer;
unsigned int input_index;

unsigned char codes[4096];
unsigned char m_for_codes[4096];
unsigned char inputs[4096];
unsigned char memory[100010];
unsigned char jumps[4096];

int stack[5000];
int infinite[5000];
int sp;
int tc;

void preprocess(void)
{
	sp = 0;
	for (int i = 0; i < csize; i++) {
		if (codes[i] == '[') {
			sp++;
			stack[sp] = i;
		}
		if (codes[i] == ']') {
			jumps[stack[sp]] = i;
			jumps[i] = stack[sp];
			sp--;
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
		if (memory[pointer] == 0) { /* loop pass */
			ret = jumps[index] + 1;
		}
		else {
			infinite[sp] = 0;
			stack[sp] = index;
			sp++;
		}
	}
	else if (codes[index] == ']') {
		if (memory[pointer] != 0) {
			ret = jumps[index] + 1;
			/* same as previous enter */
			if (m_for_codes[index] == memory[pointer]) infinite[sp-1] = tc;
			else infinite[sp-1] = 0;
		}
		else sp--;
	}
	else if (codes[index] == ',') {
		if (input_index >= isize) {
			memory[pointer] = 255;
		}
		else {
			memory[pointer] = inputs[input_index++];
		}
	} // pass "."
	m_for_codes[index] = memory[pointer];

	return ret;
}

void run(void)
{
	int max_code = 50000001;
	int index = 0;
	int i;

	pointer = 0;
	input_index = 0;
	sp = 0;

	/* terminates within 50 000 000 instructions */
	while (max_code--) {
		if (index >= csize) {
			printf("Terminates\n");
			return;
		}
		index = do_code(index);
	}

	/* at most 50 000 000 instructions within infinite loop */
	max_code = 50000001;
	while (max_code--) index = do_code(index);

	for (i = 0; i < sp; i++) {
		if (infinite[i] == tc) {
			printf("Loops %d %d\n", stack[i], jumps[stack[i]]);
			break;
		}
	}
	if (i == sp)
		printf("Loops %d %d\n", stack[sp - 1], jumps[stack[sp - 1]]);
}

void init(void)
{
	scanf("%d %d %d", &msize, &csize, &isize);

	for (int i = 0; i < msize; i++) {
		memory[i] = 0;
	}
	for (int i = 0; i < csize; i++) {
		scanf(" %c", &codes[i]);
		m_for_codes[i] = 0;
	}
	getchar();
	for (int i = 0; i < isize; i++) {
		scanf(" %c", &inputs[i]);
	}
	getchar();
}

int main(void)
{
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++) {

		/* get input & init arrays */
		init();

		/* [[ ]] find sets */
		preprocess();

		/* start codes */
		run();
	}
}