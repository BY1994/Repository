#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
3814 �������
// �� pass �ڵ�� fail �ڵ带 ���ϴ� �׽�Ʈ ���̽� ���� �ڵ�
// => �׽�Ʈ ���̽��� �������� ã�� ��������, �ݷʰ� ������ 

input)
2
5 5
4 2 3 7 6
5 4
4 2 3 7 8

output)
#1 1
#2 2

���� �߰� => 1�� ������ ���� ���� 
3 7
5 10 2

2019.10.01 PBY
*/


int pass_code(int N, int K, int* numbers)
{
	int numbers_cp[100000];
	int start = 0;
	int end = 0;
	int middle = 0;
	int last_middle = 0;
	int temp_k = 0;
	int i = 0;
	int max_value = 0;

	// inital value
	for (i = 0; i < N - 1; i++)
	{
		if ((numbers[i] - numbers[i + 1]) >= max_value)
		{
			max_value = (numbers[i] - numbers[i + 1]);
		}

		else if ((numbers[i + 1] - numbers[i]) >= max_value)
		{
			max_value = (numbers[i + 1] - numbers[i]);
		}
	}
	start = 0; // initialize
	end = max_value;
	middle = (start + end) / 2;
	last_middle = middle; // initialize

	// main (binary search)
	while (start <= end)
	{
		// test��
		//printf("%d %d %d %d %d\n", numbers_cp[0], numbers_cp[1], numbers_cp[2], numbers_cp[3], numbers_cp[4]);
		// �� ������ �迭 ���� (�̺� Ž�� �� ������ ���� �迭 ���·� ����)
		for (i = 0; i < N; i++)
		{
			numbers_cp[i] = numbers[i];
		}
		temp_k = K;
		middle = (start + end) / 2;


		// ���鼭 middle�� �ش��� ������ �� ����
		for (i = 0; i < N - 1; i++)
		{
			if ((numbers_cp[i + 1] - numbers_cp[i]) > middle)
			{
				temp_k -= ((numbers_cp[i + 1] - numbers_cp[i]) - middle);
				numbers_cp[i + 1] -= ((numbers_cp[i + 1] - numbers_cp[i]) - middle);
			}
			if (temp_k < 0)
			{
				break;
			}
		}

		for (i = N - 1; i > 0; i--)
		{
			if ((numbers_cp[i - 1] - numbers_cp[i]) > middle)
			{
				temp_k -= ((numbers_cp[i - 1] - numbers_cp[i]) - middle);
				numbers_cp[i - 1] -= ((numbers_cp[i - 1] - numbers_cp[i]) - middle);
			}
			if (temp_k < 0)
			{
				break;
			}

		}

		if (temp_k < 0)
		{
			start = middle + 1;
		}

		// ���̰��� �� �ٿ��� ��! 
		else
		{
			last_middle = middle;
			end = middle - 1;
		}
	}
	return last_middle;


}

int fail_code(int N, int K, int* numbers)
{
	int numbers_cp[100000];
	int start = 0;
	int end = 0;
	int middle = 0;
	int last_middle = 0;
	int temp_k = 0;
	int i = 0;
	int max_value = 0;

	// inital value
	for (i = 0; i < N - 1; i++)
	{
		if ((numbers[i] - numbers[i + 1]) >= max_value)
		{
			max_value = (numbers[i] - numbers[i + 1]);
		}

		else if ((numbers[i + 1] - numbers[i]) >= max_value)
		{
			max_value = (numbers[i + 1] - numbers[i]);
		}
	}
	start = 0;
	end = max_value;
	middle = (start + end) / 2 + (start + end) % 2;
	last_middle = middle;
	// main (binary search)
	while (1)
	{
		// test��
		//printf("%d %d %d %d %d\n", numbers_cp[0], numbers_cp[1], numbers_cp[2], numbers_cp[3], numbers_cp[4]);
		// �� ������ �迭 ���� (�̺� Ž�� �� ������ ���� �迭 ���·� ����)
		for (i = 0; i < N; i++)
		{
			numbers_cp[i] = numbers[i];
		}
		temp_k = K;
		// ���鼭 middle�� �ش��� ������ �� ����
		for (i = 0; i < N - 1; i++)
		{
			if ((numbers_cp[i] - numbers_cp[i + 1]) > middle)
			{
				temp_k -= ((numbers_cp[i] - numbers_cp[i + 1]) - middle);
				numbers_cp[i] -= ((numbers_cp[i] - numbers_cp[i + 1]) - middle);
			}
			else if ((numbers_cp[i + 1] - numbers_cp[i]) > middle)
			{
				temp_k -= ((numbers_cp[i + 1] - numbers_cp[i]) - middle);
				numbers_cp[i + 1] -= ((numbers_cp[i + 1] - numbers_cp[i]) - middle);
			}
		}

		// k ������ �˳��ϰ� �༭ ������ ���ϰ�
		if (temp_k < 0)
		{
			start = middle + 1;
			middle = (start + end) / 2 + (start + end) % 2;
		}
		// k ������ �ٿ��� ������ ���ϰ�! 
		else
		{
			last_middle = middle;
			end = middle - 1;
			middle = (start + end) / 2 + (start + end) % 2;
			if (start > end)
			{
				break;
			}
		}
	}

	return last_middle;
}

int main(void)
{
	// generate test case
	int test_case;
	int T = 200;
	int N, K;
	srand((unsigned)time(NULL));

	for (test_case = 1; test_case <= T; ++test_case)
	{
		// ����
		N = rand();
		K = rand();
		printf("N: %d K: %d ", N, K);

		// input
		int i = 0;
		int start = 0;
		int end = 0;
		int middle = 0;
		int last_middle = 0;
		int temp_k = 0;
		// int numbers[N]; // ���� ũ���� �迭�� �� ���
		int numbers[100000];
		//int* numbers = (int*)malloc(sizeof(int) * N); // ���� �Ҵ� (int*) �� ���̴� �Ͱ� �� ���̴� ���� ����?
		//int* numbers_cp = (int*)malloc(sizeof(int) * N);
		// null �����͸� �������ϰ� �ִٴ� ���� �޼��� �� C6011
		// https://pang2h.tistory.com/196
		if (numbers != NULL)
		{
			for (i = 0; i < N; i++)
			{
				numbers[i] = rand();
				// printf("%d ", numbers[i]);
			}
		}

		int max_value = 0;

		int pass_ans = pass_code(N, K, numbers);
		int fail_ans = fail_code(N, K, numbers);

		// output
		if (pass_ans == fail_ans) printf("#%d True\n", test_case);
		else
		{
			printf("#%d False: pass ans %d fail ans %d", test_case, pass_ans, fail_ans);
		}
	}
	return 0; //��������� �ݵ�� 0�� �����ؾ� �մϴ�.
}
