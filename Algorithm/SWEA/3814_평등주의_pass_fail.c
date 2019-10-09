#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
3814 평등주의
// 내 pass 코드와 fail 코드를 비교하는 테스트 케이스 제조 코드
// => 테스트 케이스로 차이점을 찾지 못했으나, 반례가 존재함 

input)
2
5 5
4 2 3 7 6
5 4
4 2 3 7 8

output)
#1 1
#2 2

문제 발견 => 1이 나오면 논리적 문제 
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
		// test용
		//printf("%d %d %d %d %d\n", numbers_cp[0], numbers_cp[1], numbers_cp[2], numbers_cp[3], numbers_cp[4]);
		// 돌 때마다 배열 복사 (이분 탐색 할 때마다 원래 배열 상태로 시작)
		for (i = 0; i < N; i++)
		{
			numbers_cp[i] = numbers[i];
		}
		temp_k = K;
		middle = (start + end) / 2;


		// 돌면서 middle에 해당할 때까지 다 뺀다
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

		// 차이값을 더 줄여도 됨! 
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
		// test용
		//printf("%d %d %d %d %d\n", numbers_cp[0], numbers_cp[1], numbers_cp[2], numbers_cp[3], numbers_cp[4]);
		// 돌 때마다 배열 복사 (이분 탐색 할 때마다 원래 배열 상태로 시작)
		for (i = 0; i < N; i++)
		{
			numbers_cp[i] = numbers[i];
		}
		temp_k = K;
		// 돌면서 middle에 해당할 때까지 다 뺀다
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

		// k 범위를 넉넉하게 줘서 기준을 약하게
		if (temp_k < 0)
		{
			start = middle + 1;
			middle = (start + end) / 2 + (start + end) % 2;
		}
		// k 범위를 줄여서 기준을 강하게! 
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
		// 생성
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
		// int numbers[N]; // 고정 크기의 배열일 때 사용
		int numbers[100000];
		//int* numbers = (int*)malloc(sizeof(int) * N); // 동적 할당 (int*) 을 붙이는 것과 안 붙이는 것의 차이?
		//int* numbers_cp = (int*)malloc(sizeof(int) * N);
		// null 포인터를 역참조하고 있다는 에러 메세지 뜸 C6011
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
	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}
