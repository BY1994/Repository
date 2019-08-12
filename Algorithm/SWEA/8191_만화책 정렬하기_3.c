#include<stdio.h>

// 전역변수로 할당하고나서야 런타임 에러 해결! 
int Books[200000];
int Book_Check[200001];

int main(void)
{
	// testcase
	int T;
	int i;

	scanf("%d", &T);
	
	for (i=0; i<T; i++)
	{
		// input
		int ans;
		int N;
	    
		ans = 0;
	
		scanf("%d", &N);
    
		int j;		
		
        for (j=0; j<200001; j++)
        {
            Book_Check[j] = 0;
        }
        
		// main
		for (j=0; j<N; j++)
		{
			scanf("%d", &Books[j]);
			Book_Check[Books[j]] = 1;
			if (Book_Check[Books[j]-1] == 0)
			{
				ans ++;
			}
		} 
		
		// output
		printf("#%d %d\n", i+1, ans);
	}
	
	return 0;
}

