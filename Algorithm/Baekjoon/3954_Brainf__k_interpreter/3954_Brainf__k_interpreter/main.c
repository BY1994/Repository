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
가장 안쪽 루프 말고 중간 루프가 답이도록 반례 만들어보기
1억번째에 우연히 안쪽 루프에 있도록

내가 만든 내 코드 반례
1
8 23 1
++[[[>>>>>>]<<<<<<++]+]
a

4+17*n 하면 100000001번째에 10 번째 코드 (>) 실행 중
답
Loops 3 20
=> 일반적인 풀이인 min, max 범위 적용
https://kibbomi.tistory.com/6

7. 자료형 지정 오류
그래도 틀렸는데, unsigned char 하면 형변환이 값을 이상하게 바꿨나 싶어서
int로 다 바꿨다.

=> 통과!
(memory[pointer] + 256 - 1) % 256; 이런 부분에서 형변환이 문제를 일으키는 줄 알았는데,
확인 결과 jumps[] 배열에 들어가는 값이 0~4096 index 인데,
이걸 unsigned char 로 지정해버려서 문제가 되었다.
*/

#include <stdio.h>

int msize;
int csize;
int isize;
int pointer;
int input_index;

unsigned char codes[4096];
unsigned char inputs[4096];
unsigned char memory[100010];
int jumps[4096]; // 실수한 지점, 이건 4096 index 까지 들어가야하는데 unsigned char 로 잘못 지정함

int stack[5000];
int stack_pos[5000];
int cptr;
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
			stack_pos[sp] = cptr;
			stack[sp] = index;
			sp++;
		}
	}
	else if (codes[index] == ']') {
		if (memory[pointer] != 0) {
			ret = jumps[index] + 1;
			stack_pos[sp - 1] = cptr; /* update */
		}
		else sp--; /* loop end */
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
	int i;

	pointer = 0;
	input_index = 0;
	sp = 0;
	cptr = 0;

	/* terminates within 50 000 000 instructions */
	while (max_code--) {
		if (index >= csize) {
			printf("Terminates\n");
			return;
		}
		index = do_code(index);
		cptr++;
	}

	/* at most 50 000 000 instructions within infinite loop */
	max_code = 50000001;
	while (max_code--) {
		index = do_code(index);
		cptr++;
	}

	for (i = 0; i < sp; i++) {
		if (cptr-1-stack_pos[i] <= 50000000) {
			printf("Loops %d %d\n", stack[i], jumps[stack[i]]);
			break;
		}
	}
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