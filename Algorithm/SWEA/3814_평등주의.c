#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
// 사용가능한 라이브러리 여부 확인

/*
3814 평등주의

input)
2
5 5
4 2 3 7 6
5 4
4 2 3 7 8

output)
#1 1
#2 2

문제 발견
5 3
7 3 4 5 6
하면 1이 나와야하는데 2가 나옴

2019.10.01
*/

int ABS(int v) {return v>0 ? v : -v;}

int main()
{
	// unsafe error
	// https://bymakers.tistory.com/6
	//freopen("./input.txt", "r", stdin);
	// input
	int T, N, K;
	int t = 0;
	int i = 0;
	int start = 0;
	int end = 0;
	int middle = 0;
	int last_middle = 0;
	int temp_k = 0;
	scanf_s("%d", &T);
	for (t = 0; t < T; t++)
	{

		scanf_s("%d %d", &N, &K);
		// int numbers[N]; // 고정 크기의 배열일 때 사용
		int *numbers = (int*)malloc(sizeof(int)*N); // 동적 할당 (int*) 을 붙이는 것과 안 붙이는 것의 차이?
		int* numbers_cp = (int*)malloc(sizeof(int) * N);
		// null 포인터를 역참조하고 있다는 에러 메세지 뜸 C6011
		// https://pang2h.tistory.com/196
		if (numbers != NULL)
		{
			for (i = 0; i < N; i++)
			{
				scanf_s("%d", &numbers[i]);
			}
		}

		int max_value = 0;

		// inital value
		for (i = 0; i < N-1; i++)
		{
			if ((numbers[i] - numbers[i+1]) >= max_value)
			{
				max_value = (numbers[i]-numbers[i+1]);
			}

			else if ((numbers[i+1] - numbers[i]) >= max_value)
			{
				max_value = (numbers[i+1] - numbers[i]);
			}
		}
		start = 0;
		end = max_value;
		middle = (start + end) / 2 + (start + end) % 2;
		last_middle = 0;
		
		// main (binary search)
		while (start < end)
		{
			
			// test용
			//printf("%d %d %d %d %d\n", numbers_cp[0], numbers_cp[1], numbers_cp[2], numbers_cp[3], numbers_cp[4]);
			// 돌 때마다 배열 복사 (이분 탐색 할 때마다 원래 배열 상태로 시작)
			
			for (i = 0; i < N; i++)
			{
				numbers_cp[i] = numbers[i];
			}
			temp_k = K;
			last_middle = middle;
			middle = (start + end) / 2;

			// 돌면서 middle에 해당할 때까지 다 뺀다
			for (i = 0; i < N - 1; i++)
			{
				if ((numbers_cp[i+1] - numbers_cp[i]) > middle)
				{
					temp_k -= ((numbers_cp[i+1] - numbers_cp[i]) - middle);
					numbers_cp[i+1] -= ((numbers_cp[i+1] - numbers_cp[i]) - middle);
				}
				if (temp_k < 0)
				{
					break;
				}
			}
			
			printf("1\n");
			printf("middle : %d   end : %d    start : %d  \n", middle, end, start);
			int aa;
			for(aa = 0; aa< N; aa++){
				printf("%d, ", numbers_cp[aa]);
			} 
			printf("\n\n");
			
			for (i = N-1; i > 0; i--)
			{
				printf("i : %d   diff : %d\n", i ,numbers_cp[i] - numbers_cp[i-1]);
				if ((numbers_cp[i-1] - numbers_cp[i]) > middle)
				{
					temp_k -= ((numbers_cp[i-1] - numbers_cp[i]) - middle);
					numbers_cp[i-1] -= ((numbers_cp[i-1] - numbers_cp[i]) - middle);
				}
				
				if (temp_k < 0)
				{
					break;
				}
			}
			
			printf("2\n");
			printf("middle : %d   end : %d    start : %d  \n", middle, end, start);
			for(aa = 0; aa< N; aa++){
				printf("%d, ", numbers_cp[aa]);
			} 
			printf("\n\n");

			// 차이값을 더 크게 잡음 (이 범위에는 답이 없다)
			if (temp_k < 0)
			{
				start = middle + 1;
			}
			
			// 차이값을 더 줄여도 됨! 
			else
			{
				end = middle;
			}
		}

		// output
		printf("#%d %d\n", t+1, last_middle);
	}

	/*
	동적 할당
	https://mrsnake.tistory.com/45
	*/
	return 0;
}
