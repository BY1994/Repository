#include <stdio.h>

/* 
ans[0] = col[0]; 이라고 잘못 썼는데 예제는 맞아서 문제를 발견 못했다... 

모범 풀이
#include<cstdio>
int main(){int a[6];for(int i=0;i<6;i++)scanf("%d",&a[i]);printf("%d %d",a[0]^a[2]^a[4],a[1]^a[3]^a[5]);} 
*/

int row[3], col[3];
int ans[2];

int main(void)
{
	for (int i = 0; i < 3; i++)
		scanf("%d %d", &row[i], &col[i]);
	
	if (row[0] == row[1]) ans[0] = row[2];
	else if (row[0] != row[1] && row[1] != row[2]) ans[0] = row[1];
	else ans[0] = row[0];
	
	if (col[0] == col[1]) ans[1] = col[2];
	else if (col[0] != col[1] && col[1] != col[2]) ans[1] = col[1];
	else ans[1] = col[0];
	
	printf("%d %d\n", ans[0], ans[1]);
	return 0;
}
