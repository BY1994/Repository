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
		int index;
		int N;
		
		ans = 0;
		index = -1;
	
		scanf("%d", &N);
	
		int Books[N];
		int j;		
	
		for (j=0; j<N; j++)
		{
			scanf("%d", &Books[j]);
		} 
		
		// function
		void moveBook(baseline)
		{
			ans++;
			while (1)
			{
				if (index+1 < N)
				{
					index++;
					if (Books[index] == baseline+1)
					{
						baseline++;
					}
					else if (Books[index] < baseline+1)
					{
						moveBook(Books[index]);
					}
					else
					{
						return;
					}
				}
				else
				{
					return;
				}
			}
		}
		
		// main loop
		while (1)
		{
			if (index+1 < N)
			{
				index++;
				moveBook(Books[index]);
			}
			else
			{
				break;
			}
		}
		
		// output
		printf("#%d %d\n", i+1, ans);
	}
	
	return 0;
}
