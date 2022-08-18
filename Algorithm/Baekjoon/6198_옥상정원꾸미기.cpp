/*
6198 �������� �ٹ̱�
�� ���� 1~8�� ���� ���̶� int ���� �Ѿ�µ� ��� �����ؼ� ������
https://www.acmicpc.net/board/view/91640

���� Ǯ�̸� ���� ������ �����ϴ� �迭�� �� �ʿ䰡 ������
������ ���̰� �̹� ���̴� �����̱� ������
����
https://www.acmicpc.net/source/34946146
*/
#include <stdio.h>

int buildings[80001];
struct _stack {
	int id;
	int len;
	int count;
}stack[80001];
int sp;

int main(void)
{
	int N, h;
	long long count = 0LL;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &h);
		while (sp > 0 && stack[sp-1].len <= h) {
			sp--;
			buildings[stack[sp].id] = stack[sp].count;
			if (sp > 0) stack[sp-1].count += stack[sp].count + 1;
		}
		stack[sp++] = {i, h, 0};
	}
	while (sp) {
		sp--;
		buildings[stack[sp].id] = stack[sp].count;
		if (sp > 0) stack[sp-1].count += stack[sp].count + 1;
	}
	for (int i = 0; i < N; i++) {
		count += buildings[i];
	}
	printf("%lld\n", count);
	return 0;
}

// https://www.acmicpc.net/source/34946146
/*
import sys
def solve():
    N = int(sys.stdin.readline())
    stack = []
    result = 0

    for _ in range(N):
        building = int(sys.stdin.readline())

        while stack and stack[-1] <= building:
            stack.pop()
        result += len(stack)
        stack.append(building)

    print(result)

solve()
*/