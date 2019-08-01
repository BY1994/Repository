#include <stdio.h>
// #include <stdlib.h>

int main(void)
{
	int test_case;
	int T;
	int N, A, B;
	
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		// input
		scanf("%d %d %d", &N, &A, &B);
		int letters[N];
		int timeTable[1001] = {0,};
		int i, j;
		int letterIndex = 0;
		for (i=0; i<N; ++i)
		{
			scanf("%d", &letters[i]);
			timeTable[letters[i]] = 1;
		}
		printf("#%d", test_case);
		
		// 1000 시간 확인
		int numLetter = 0;
		int latest = letters[letterIndex];
		
		for (i=0; i<1001; ++i)
		{
			// 1000 시간 다 확인할 필요 없음 
			if (letterIndex == N)
			{
				break;
			}
			
			// 편지 배달받음 
			if (timeTable[i] == 1)
			{
				numLetter++;
			}
			
			// 우편함 비우기
			if ((numLetter == A)||(latest == i-B))
			{
				for (j=0; j<numLetter/2+numLetter%2; ++j)
				{
					printf(" %d", i);
				}
				letterIndex += numLetter/2 + numLetter %2;
				if (letterIndex > N-1)
				{
					break;
				}
				latest = letters[letterIndex];
				numLetter -= numLetter/2 + numLetter%2;

			}  
		}
		printf("\n"); 
	}
	// system("PAUSE");
	return 0;
}
