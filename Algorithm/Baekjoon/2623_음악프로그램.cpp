#include <stdio.h>

/*
void push_q(int input)
{
	queue[e] = input;
	e++;
}
�� �Ǽ� queue�� e++ �� ���� ���.... �׷��� ���� �� ��� ���� ������..
*/

int N, M, S, pre, next;
int singer[1002][1002];
int inDegree[1002];
int result[1002];
int queue[100000], s, e;

void get_input(void)
{
	for (int i = 0; i < M; i++)
	{
		scanf("%d", &S);
		scanf("%d", &pre);
		for (int j = 0; j < S - 1; j++)
		{
			scanf("%d", &next);
			// pre�� next�� ����ؼ� �ֱ�
			singer[pre][next]++;
			if (singer[pre][next] == 1) inDegree[next]++;
			pre = next;
		}
	}
}

void push_q(int input)
{
	queue[e] = input;
	e++;
}

int pop_q(void)
{
	int ret = queue[s];
	s++;
	return ret;
}

int topoloy_sort(void)
{
	// queue�� �ֱ�
	for (int i = 1; i <= N; i++)
	{
		if (inDegree[i] == 0) push_q(i);
	}

	for (int i = 0; i < N; i++)
	{
		if (s == e) return 0; // queue�� �߰��� ����ٸ�...
		int cur_singer = pop_q();
		result[i] = cur_singer;
		// ���鼭 ���� �ĺ� ã��
		for (int j = 1; j <= N; j++)
		{
			if (singer[cur_singer][j] >= 1 && --inDegree[j] == 0)
				push_q(j);
		}
	}
	return 1;
}

void print_result(void)
{
	for (int i = 0; i < N; i++)
		printf("%d\n", result[i]);
}

int main(void)
{
	scanf("%d %d", &N, &M);
	get_input();
	if (topoloy_sort()) print_result();
	else printf("%d\n", 0);
	return 0;
}