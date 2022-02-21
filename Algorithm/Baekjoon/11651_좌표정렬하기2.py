"""
11651 좌표 정렬하기 2
"""

coord = []
n = int(input())
for i in range(n):
    coord.append(list(map(int, input().split())))

coord.sort(key = lambda x:(x[1], x[0]))

for i in range(n):
    print(*coord[i])


# 시간초과
"""
#include <stdio.h>

int input[100010][2];

void quickSort(int first, int last)
{
	int pivot;
	int i;
	int j;
	int temp;
	
	if (first < last)
	{
		pivot = first;
		i = first;
		j = last;

		while (i < j)
		{
			while ((input[i][1] < input[pivot][1] || \
    			(input[i][1] == input[pivot][1] && input[i][0] <= input[pivot][0])) \
    			&& i < last)
			{
				i++;
			}
			while ((input[j][1] > input[pivot][1] || \
			    (input[j][1] == input[pivot][1] && input[j][0] > input[pivot][0])))
			{
				j--;
			}
			if (i < j)
			{
				temp = input[i][0];
				input[i][0] = input[j][0];
				input[j][0] = temp;
				
				temp = input[i][1];
				input[i][1] = input[j][1];
				input[j][1] = temp;
			}
		}

		temp = input[pivot][0];
		input[pivot][0] = input[j][0];
		input[j][0] = temp;
		
		temp = input[pivot][1];
		input[pivot][1] = input[j][1];
		input[j][1] = temp;

		quickSort(first, j - 1);
		quickSort(j + 1, last);
	}
}

int main()
{
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &input[i][0], &input[i][1]);
    }
    quickSort(0, n-1);
    
    for (int i = 0; i < n; i++) {
        printf("%d %d\n", input[i][0], input[i][1]);
    }

    return 0;
}
"""

# https://www.acmicpc.net/source/38533002
"""
import sys
points = sys.stdin.readlines()[1:]
points.sort(key=lambda y:int(y.split()[0])) 
points.sort(key=lambda x : int(x.split()[1]))
print(''.join(points))
"""
