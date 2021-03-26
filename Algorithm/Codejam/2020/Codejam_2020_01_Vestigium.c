#include <stdio.h>

/*
TC

3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

*/

int TC, N;
int visitedR[101][101]; // visited 체크는 각 줄번호로 하기 
int visitedC[101][101];
int repeatedR[101], repeatedC[101];

int main(void)
{
	int tc, r, c, i, j;
	scanf("%d", &TC);
	for (tc = 1; tc<=TC; tc++)
	{
		int sum = 0, element;
		int sumR = 0, sumC = 0;
		
		for (i = 1; i<=N; i++)
		{
			for (j = 1; j<=N; j++)
			{
				visitedR[i][j] = 0;
				visitedC[i][j] = 0;
			}
			repeatedR[i] = 0;
			repeatedC[i] = 0;
		}
		scanf("%d", &N);
		// N x N만큼 돌면서 채우기, r=c 면 sum에 넣고
		for (r = 1; r<=N; r++)
		{
			for (c = 1; c <= N; c++)
			{
				scanf("%d", &element);
				if (r == c) sum += element;
				
				// row repated
				if (visitedR[r][element] == 1) repeatedR[r] = 1;
				visitedR[r][element] = 1;
				
				// col repeated
				if (visitedC[c][element] == 1) repeatedC[c] = 1;
				visitedC[c][element] = 1; 
			}
		}
		
		for (i = 1; i<=N; i++)
		{
			sumR += repeatedR[i];
			sumC += repeatedC[i];
		}
		
		printf("Case #%d: %d %d %d\n", tc, sum, sumR, sumC);
	}
	return 0;
}
