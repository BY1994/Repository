#include<stdio.h>

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
    
		int Books[N];
		int Book_Check[200001] = {0};
		int j;		
		
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

