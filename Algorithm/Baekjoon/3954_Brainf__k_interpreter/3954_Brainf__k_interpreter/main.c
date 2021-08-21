/*
3954 brain f**k interpreter
1. %c �� �޴� ��� \n ���๮�ڰ� ���� �޾�����
input�� �̻��ϰ� �޾�����. getchar() �� ���̿� �ְ� �ذ�
2. code max ���� 50000000 ���� �� �� edge case�� �ɷȴ�.
1�� �߰��ؼ� �ݷʸ� �����.
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
3. Loops ���� => ���� �ֱ� ������ �ϸ� �� ��
https://www.acmicpc.net/board/view/9096
���ѷ����� �ش��ϴ� ������ �ֱٿ� �ִ� ������� ������ �����ϴ�.
����, +[+[-]] ���� ���� ��ø ������ ������ ���� ���� �ٱ� ��������, �쿬�� 5õ�� ��° ���� �߿� ���� ���� ������ �����ϰ� �־��ٸ� ���� ������ ������ ����ع��� ���Դϴ�.
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