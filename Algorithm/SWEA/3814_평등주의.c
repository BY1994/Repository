#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
// ��밡���� ���̺귯�� ���� Ȯ��

/*
3814 �������

input)
2
5 5
4 2 3 7 6
5 4
4 2 3 7 8

output)
#1 1
#2 2

���� �߰�
5 3
7 3 4 5 6
�ϸ� 1�� ���;��ϴµ� 2�� ����

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
		// int numbers[N]; // ���� ũ���� �迭�� �� ���
		int *numbers = (int*)malloc(sizeof(int)*N); // ���� �Ҵ� (int*) �� ���̴� �Ͱ� �� ���̴� ���� ����?
		int* numbers_cp = (int*)malloc(sizeof(int) * N);
		// null �����͸� �������ϰ� �ִٴ� ���� �޼��� �� C6011
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
			
			// test��
			//printf("%d %d %d %d %d\n", numbers_cp[0], numbers_cp[1], numbers_cp[2], numbers_cp[3], numbers_cp[4]);
			// �� ������ �迭 ���� (�̺� Ž�� �� ������ ���� �迭 ���·� ����)
			
			for (i = 0; i < N; i++)
			{
				numbers_cp[i] = numbers[i];
			}
			temp_k = K;
			last_middle = middle;
			middle = (start + end) / 2;

			// ���鼭 middle�� �ش��� ������ �� ����
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

			// ���̰��� �� ũ�� ���� (�� �������� ���� ����)
			if (temp_k < 0)
			{
				start = middle + 1;
			}
			
			// ���̰��� �� �ٿ��� ��! 
			else
			{
				end = middle;
			}
		}

		// output
		printf("#%d %d\n", t+1, last_middle);
	}

	/*
	���� �Ҵ�
	https://mrsnake.tistory.com/45
	*/
	return 0;
}
